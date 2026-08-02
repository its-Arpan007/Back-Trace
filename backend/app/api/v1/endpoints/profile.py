from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.profile import (
    UserProfileResponse,
    ProfileUpdateRequest,
    PreferencesUpdateRequest,
)
from app.services.profile_service import ProfileService
from app.models.user import UserModel
from app.core.security.dependencies import get_current_user

router = APIRouter(prefix="/profile", tags=["User Profiles & Preferences"])


@router.get("", response_model=BaseResponse[UserProfileResponse])
async def get_profile(
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[UserProfileResponse]:
    service = ProfileService(db)
    profile_data = await service.get_user_profile(current_user)
    return BaseResponse(
        success=True,
        message="Profile details retrieved",
        code="PROFILE_RETRIEVED",
        data=profile_data,
    )


@router.put("", response_model=BaseResponse[UserProfileResponse])
async def update_profile(
    req: ProfileUpdateRequest,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[UserProfileResponse]:
    service = ProfileService(db)
    updated_profile = await service.update_profile(current_user, req)
    return BaseResponse(
        success=True,
        message="Profile updated successfully",
        code="PROFILE_UPDATED",
        data=updated_profile,
    )


@router.put("/preferences", response_model=BaseResponse[dict])
async def update_preferences(
    req: PreferencesUpdateRequest,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[dict]:
    if req.theme:
        current_user.theme_preference = req.theme
    if req.language:
        current_user.language = req.language
    db.add(current_user)

    return BaseResponse(
        success=True,
        message="Preferences updated successfully",
        code="PREFERENCES_UPDATED",
        data={"theme": current_user.theme_preference, "language": current_user.language},
    )


@router.put("/photo", response_model=BaseResponse[dict])
async def update_profile_photo(
    photo_url: str,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> BaseResponse[dict]:
    current_user.profile_photo = photo_url
    db.add(current_user)
    return BaseResponse(
        success=True,
        message="Profile photo updated successfully",
        code="PHOTO_UPDATED",
        data={"profile_photo": photo_url},
    )
