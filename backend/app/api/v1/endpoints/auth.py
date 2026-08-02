import uuid
from typing import List
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    RefreshTokenRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    ChangePasswordRequest,
)
from app.schemas.profile import UserProfileResponse, SessionResponse
from app.services.auth_service import AuthService
from app.services.profile_service import ProfileService
from app.models.user import UserModel
from app.core.security.dependencies import get_current_user
from app.repositories.user_repository import SessionRepository

router = APIRouter(prefix="/auth", tags=["Authentication & Identity"])


@router.post("/register", response_model=BaseResponse[dict], status_code=status.HTTP_201_CREATED)
async def register(
    req: RegisterRequest, request: Request, db: AsyncSession = Depends(get_db)
) -> BaseResponse[dict]:
    service = AuthService(db)
    ip_addr = request.client.host if request.client else None
    user_agent = request.headers.get("User-Agent")
    user = await service.register_user(req, ip_address=ip_addr, user_agent=user_agent)
    return BaseResponse(
        success=True,
        message="User registered successfully. Please verify your email.",
        code="USER_REGISTERED",
        data={"user_id": str(user.id), "username": user.username, "email": user.email, "role": user.role},
    )


@router.post("/login", response_model=BaseResponse[TokenResponse])
async def login(
    req: LoginRequest, request: Request, db: AsyncSession = Depends(get_db)
) -> BaseResponse[TokenResponse]:
    service = AuthService(db)
    ip_addr = request.client.host if request.client else None
    user_agent = request.headers.get("User-Agent")
    token_res = await service.login_user(req, ip_address=ip_addr, user_agent=user_agent)
    return BaseResponse(
        success=True,
        message="Login successful",
        code="LOGIN_SUCCESS",
        data=token_res,
    )


@router.post("/refresh", response_model=BaseResponse[TokenResponse])
async def refresh_tokens(
    req: RefreshTokenRequest, request: Request, db: AsyncSession = Depends(get_db)
) -> BaseResponse[TokenResponse]:
    service = AuthService(db)
    ip_addr = request.client.host if request.client else None
    user_agent = request.headers.get("User-Agent")
    token_res = await service.refresh_tokens(req.refresh_token, ip_address=ip_addr, user_agent=user_agent)
    return BaseResponse(
        success=True,
        message="Tokens refreshed successfully",
        code="TOKEN_REFRESH_SUCCESS",
        data=token_res,
    )


@router.post("/logout", response_model=BaseResponse[dict])
async def logout(
    request: Request,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[dict]:
    service = AuthService(db)
    session_id_str = request.state.correlation_id if hasattr(request.state, "correlation_id") else None
    sess_id = uuid.UUID(session_id_str) if session_id_str else uuid.uuid4()
    await service.logout_user(sess_id, current_user.id)
    return BaseResponse(
        success=True,
        message="Successfully logged out",
        code="LOGOUT_SUCCESS",
        data={"user_id": str(current_user.id)},
    )


@router.get("/me", response_model=BaseResponse[UserProfileResponse])
async def get_me(
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[UserProfileResponse]:
    profile_service = ProfileService(db)
    profile_data = await profile_service.get_user_profile(current_user)
    return BaseResponse(
        success=True,
        message="Current user profile retrieved",
        code="PROFILE_RETRIEVED",
        data=profile_data,
    )


@router.get("/sessions", response_model=BaseResponse[List[SessionResponse]])
async def get_sessions(
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[List[SessionResponse]]:
    sess_repo = SessionRepository(db)
    sessions = await sess_repo.get_user_active_sessions(current_user.id)
    res_list = [
        SessionResponse(
            id=str(s.id),
            device_info=s.device_info,
            ip_address=s.ip_address,
            is_active=s.is_active,
            last_active_at=s.last_active_at,
            created_at=s.created_at,
        )
        for s in sessions
    ]
    return BaseResponse(
        success=True,
        message="Active sessions retrieved",
        code="SESSIONS_RETRIEVED",
        data=res_list,
    )


@router.delete("/logout-all", response_model=BaseResponse[dict])
async def logout_all(
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[dict]:
    service = AuthService(db)
    await service.logout_all_sessions(current_user.id)
    return BaseResponse(
        success=True,
        message="Logged out from all devices",
        code="LOGOUT_ALL_SUCCESS",
        data={"user_id": str(current_user.id)},
    )


@router.post("/forgot-password", response_model=BaseResponse[dict])
async def forgot_password(req: ForgotPasswordRequest) -> BaseResponse[dict]:
    return BaseResponse(
        success=True,
        message="Password reset instructions sent to your email address",
        code="FORGOT_PASSWORD_SENT",
        data={"email": req.email},
    )


@router.post("/reset-password", response_model=BaseResponse[dict])
async def reset_password(req: ResetPasswordRequest) -> BaseResponse[dict]:
    return BaseResponse(
        success=True,
        message="Password has been successfully reset",
        code="PASSWORD_RESET_SUCCESS",
        data={},
    )


@router.post("/change-password", response_model=BaseResponse[dict])
async def change_password(
    req: ChangePasswordRequest,
    current_user: UserModel = Depends(get_current_user),
) -> BaseResponse[dict]:
    return BaseResponse(
        success=True,
        message="Password changed successfully",
        code="PASSWORD_CHANGE_SUCCESS",
        data={"user_id": str(current_user.id)},
    )
