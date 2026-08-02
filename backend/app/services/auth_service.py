from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple, List, Dict, Any
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import (
    UnauthorizedException,
    ValidationException,
    NotFoundException,
)
from app.core.security import get_password_hash, verify_password
from app.core.security.jwt import create_token_pair, hash_token, decode_token
from app.models.user import UserModel, SessionModel
from app.repositories.user_repository import (
    UserRepository,
    SessionRepository,
    RefreshTokenRepository,
    AuditLogRepository,
)
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)


class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)
        self.session_repo = SessionRepository(db)
        self.token_repo = RefreshTokenRepository(db)
        self.audit_repo = AuditLogRepository(db)

    async def register_user(
        self, req: RegisterRequest, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> UserModel:
        existing = await self.user_repo.get_by_email_or_username(req.email)
        if existing:
            await self.audit_repo.log_action(
                action="REGISTER_FAILED_DUPLICATE_EMAIL",
                ip_address=ip_address,
                user_agent=user_agent,
                details={"email": req.email},
            )
            raise ValidationException("An account with this email already exists.")

        existing_user = await self.user_repo.get_by_email_or_username(req.username)
        if existing_user:
            raise ValidationException("Username is already taken.")

        user_data = {
            "first_name": req.first_name,
            "last_name": req.last_name,
            "username": req.username,
            "email": req.email,
            "password_hash": get_password_hash(req.password),
            "phone_number": req.phone_number,
            "role": req.role,
            "timezone": req.timezone,
            "language": req.language,
        }

        user = await self.user_repo.create_user_with_role_profile(user_data, req.role)

        await self.audit_repo.log_action(
            action="USER_REGISTERED",
            user_id=user.id,
            ip_address=ip_address,
            user_agent=user_agent,
            details={"role": req.role, "email": req.email},
        )
        return user

    async def login_user(
        self, req: LoginRequest, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> TokenResponse:
        user = await self.user_repo.get_by_email_or_username(req.username_or_email)
        if not user or not verify_password(req.password, user.password_hash):
            await self.audit_repo.log_action(
                action="LOGIN_FAILED_INVALID_CREDENTIALS",
                ip_address=ip_address,
                user_agent=user_agent,
                details={"identifier": req.username_or_email},
            )
            raise UnauthorizedException("Invalid username/email or password.")

        if user.status != "active":
            raise UnauthorizedException("Account is inactive or suspended.")

        # Create Session
        expires_days = 30 if req.remember_me else 7
        sess_expires_at = datetime.now(timezone.utc) + timedelta(days=expires_days)
        sess = await self.session_repo.create_session(
            user_id=user.id,
            device_info=req.device_info,
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=sess_expires_at,
        )

        # Create Token Pair
        access_token, refresh_token, token_expires_at = create_token_pair(
            user_id=str(user.id),
            role=user.role,
            session_id=str(sess.id),
        )

        # Store Refresh Token Hash
        t_hash = hash_token(refresh_token)
        await self.token_repo.save_token(
            user_id=user.id,
            session_id=sess.id,
            token_hash=t_hash,
            expires_at=token_expires_at,
        )

        # Update last login
        user.last_login = datetime.now(timezone.utc)
        self.db.add(user)

        await self.audit_repo.log_action(
            action="USER_LOGGED_IN",
            user_id=user.id,
            ip_address=ip_address,
            user_agent=user_agent,
            details={"session_id": str(sess.id), "device_info": req.device_info},
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=60 * 24 * 8 * 60,
            session_id=str(sess.id),
            user_id=str(user.id),
            role=user.role,
        )

    async def refresh_tokens(
        self, refresh_token: str, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
            if payload.get("type") != "refresh":
                raise UnauthorizedException("Invalid token type")
            user_id = uuid.UUID(payload.get("sub"))
            session_id = uuid.UUID(payload.get("session_id"))
        except Exception:
            raise UnauthorizedException("Invalid or expired refresh token")

        t_hash = hash_token(refresh_token)
        token_record = await self.token_repo.get_valid_token(t_hash)
        if not token_record:
            raise UnauthorizedException("Refresh token is revoked or expired")

        # Revoke old refresh token (Token Rotation)
        await self.token_repo.revoke_token(t_hash)

        user = await self.user_repo.get_user_with_profiles(user_id)
        if not user:
            raise NotFoundException("User", user_id)

        # Mint new token pair
        new_access_token, new_refresh_token, token_expires_at = create_token_pair(
            user_id=str(user.id),
            role=user.role,
            session_id=str(session_id),
        )

        new_t_hash = hash_token(new_refresh_token)
        await self.token_repo.save_token(
            user_id=user.id,
            session_id=session_id,
            token_hash=new_t_hash,
            expires_at=token_expires_at,
        )

        await self.audit_repo.log_action(
            action="TOKEN_REFRESHED",
            user_id=user.id,
            ip_address=ip_address,
            user_agent=user_agent,
            details={"session_id": str(session_id)},
        )

        return TokenResponse(
            access_token=new_access_token,
            refresh_token=new_refresh_token,
            expires_in=60 * 24 * 8 * 60,
            session_id=str(session_id),
            user_id=str(user.id),
            role=user.role,
        )

    async def logout_user(
        self, session_id: uuid.UUID, user_id: uuid.UUID, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> bool:
        await self.session_repo.revoke_session(session_id)
        await self.audit_repo.log_action(
            action="USER_LOGGED_OUT",
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
            details={"session_id": str(session_id)},
        )
        return True

    async def logout_all_sessions(
        self, user_id: uuid.UUID, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> bool:
        await self.session_repo.revoke_all_user_sessions(user_id)
        await self.audit_repo.log_action(
            action="USER_LOGGED_OUT_ALL_DEVICES",
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
        )
        return True
