import uuid
from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserModel
from app.repositories.user_repository import UserRepository, AuditLogRepository
from app.schemas.profile import UserProfileResponse, ProfileUpdateRequest, PreferencesUpdateRequest


class ProfileService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)
        self.audit_repo = AuditLogRepository(db)

    async def get_user_profile(self, user: UserModel) -> UserProfileResponse:
        student_data = None
        if user.student_profile:
            p = user.student_profile
            student_data = {
                "education_level": p.education_level,
                "institution": p.institution,
                "course": p.course,
                "semester": p.semester,
                "subjects": p.subjects or [],
                "learning_preferences": p.learning_preferences or {},
                "accessibility_preferences": p.accessibility_preferences or {},
                "current_mastery_snapshot": p.current_mastery_snapshot or {},
                "learning_streak": p.learning_streak,
                "total_questions_solved": p.total_questions_solved,
                "current_diagnostic_score": p.current_diagnostic_score,
                "current_recommendation_queue": p.current_recommendation_queue or [],
            }

        teacher_data = None
        if user.teacher_profile:
            t = user.teacher_profile
            teacher_data = {
                "institution": t.institution,
                "department": t.department,
                "subjects": t.subjects or [],
                "assigned_classes": t.assigned_classes or [],
                "years_of_experience": t.years_of_experience,
                "verification_status": t.verification_status,
            }

        admin_data = None
        if user.admin_profile:
            a = user.admin_profile
            admin_data = {
                "organization": a.organization,
                "permission_level": a.permission_level,
                "system_privileges": a.system_privileges or [],
            }

        return UserProfileResponse(
            id=str(user.id),
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            phone_number=user.phone_number,
            profile_photo=user.profile_photo,
            role=user.role,
            status=user.status,
            email_verified=user.email_verified,
            account_verified=user.account_verified,
            timezone=user.timezone,
            language=user.language,
            theme_preference=user.theme_preference,
            created_at=user.created_at,
            last_login=user.last_login,
            student_profile=student_data,
            teacher_profile=teacher_data,
            admin_profile=admin_data,
        )

    async def update_profile(
        self, user: UserModel, req: ProfileUpdateRequest
    ) -> UserProfileResponse:
        if req.first_name:
            user.first_name = req.first_name
        if req.last_name:
            user.last_name = req.last_name
        if req.phone_number:
            user.phone_number = req.phone_number
        if req.timezone:
            user.timezone = req.timezone
        if req.language:
            user.language = req.language

        if req.student_profile and user.student_profile:
            sp = req.student_profile
            p = user.student_profile
            if sp.education_level is not None:
                p.education_level = sp.education_level
            if sp.institution is not None:
                p.institution = sp.institution
            if sp.course is not None:
                p.course = sp.course
            if sp.semester is not None:
                p.semester = sp.semester
            if sp.subjects:
                p.subjects = sp.subjects
            if sp.learning_preferences:
                p.learning_preferences = sp.learning_preferences
            if sp.accessibility_preferences:
                p.accessibility_preferences = sp.accessibility_preferences

        self.db.add(user)
        await self.audit_repo.log_action(
            action="PROFILE_UPDATED",
            user_id=user.id,
            details={"updated_fields": [k for k, v in req.model_dump().items() if v is not None]},
        )
        return await self.get_user_profile(user)
