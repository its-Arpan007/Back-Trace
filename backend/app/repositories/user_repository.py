from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
import uuid
from sqlalchemy import select, update, delete, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.user import (
    UserModel,
    StudentProfileModel,
    TeacherProfileModel,
    AdminProfileModel,
    SessionModel,
    RefreshTokenModel,
    AuditLogModel,
    UserPreferencesModel,
)
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[UserModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(UserModel, session)

    async def get_by_email_or_username(self, identifier: str) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(or_(UserModel.email == identifier, UserModel.username == identifier))
            .options(
                selectinload(UserModel.student_profile),
                selectinload(UserModel.teacher_profile),
                selectinload(UserModel.admin_profile),
                selectinload(UserModel.preferences),
            )
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_user_with_profiles(self, user_id: uuid.UUID) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(UserModel.id == user_id)
            .options(
                selectinload(UserModel.student_profile),
                selectinload(UserModel.teacher_profile),
                selectinload(UserModel.admin_profile),
                selectinload(UserModel.preferences),
            )
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def create_user_with_role_profile(
        self, user_data: Dict[str, Any], role: str
    ) -> UserModel:
        user = UserModel(**user_data)
        self.session.add(user)
        await self.session.flush()

        if role == "student":
            profile = StudentProfileModel(student_id=user.id)
            self.session.add(profile)
        elif role == "teacher":
            profile = TeacherProfileModel(teacher_id=user.id)
            self.session.add(profile)
        elif role == "admin":
            profile = AdminProfileModel(admin_id=user.id)
            self.session.add(profile)

        pref = UserPreferencesModel(user_id=user.id)
        self.session.add(pref)

        await self.session.flush()
        await self.session.refresh(user)
        return user


class SessionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(
        self, user_id: uuid.UUID, device_info: Optional[str], ip_address: Optional[str], user_agent: Optional[str], expires_at: datetime
    ) -> SessionModel:
        sess = SessionModel(
            user_id=user_id,
            device_info=device_info,
            ip_address=ip_address,
            user_agent=user_agent,
            is_active=True,
            expires_at=expires_at,
        )
        self.session.add(sess)
        await self.session.flush()
        return sess

    async def get_user_active_sessions(self, user_id: uuid.UUID) -> List[SessionModel]:
        query = select(SessionModel).where(
            SessionModel.user_id == user_id, SessionModel.is_active == True
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def revoke_session(self, session_id: uuid.UUID) -> bool:
        query = (
            update(SessionModel)
            .where(SessionModel.id == session_id)
            .values(is_active=False)
        )
        await self.session.execute(query)
        return True

    async def revoke_all_user_sessions(self, user_id: uuid.UUID) -> bool:
        query = (
            update(SessionModel)
            .where(SessionModel.user_id == user_id)
            .values(is_active=False)
        )
        await self.session.execute(query)
        return True


class RefreshTokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_token(
        self, user_id: uuid.UUID, session_id: uuid.UUID, token_hash: str, expires_at: datetime
    ) -> RefreshTokenModel:
        token = RefreshTokenModel(
            user_id=user_id,
            session_id=session_id,
            token_hash=token_hash,
            is_revoked=False,
            expires_at=expires_at,
        )
        self.session.add(token)
        await self.session.flush()
        return token

    async def get_valid_token(self, token_hash: str) -> Optional[RefreshTokenModel]:
        query = select(RefreshTokenModel).where(
            RefreshTokenModel.token_hash == token_hash,
            RefreshTokenModel.is_revoked == False,
            RefreshTokenModel.expires_at > datetime.now(timezone.utc),
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def revoke_token(self, token_hash: str) -> bool:
        query = (
            update(RefreshTokenModel)
            .where(RefreshTokenModel.token_hash == token_hash)
            .values(is_revoked=True)
        )
        await self.session.execute(query)
        return True


class AuditLogRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def log_action(
        self,
        action: str,
        user_id: Optional[uuid.UUID] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> AuditLogModel:
        audit = AuditLogModel(
            user_id=user_id,
            action=action,
            ip_address=ip_address,
            user_agent=user_agent,
            details=details or {},
        )
        self.session.add(audit)
        await self.session.flush()
        return audit
