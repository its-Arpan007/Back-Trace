from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, EmailStr


class StudentProfileSchema(BaseModel):
    education_level: Optional[str] = None
    institution: Optional[str] = None
    course: Optional[str] = None
    semester: Optional[int] = None
    subjects: List[str] = []
    learning_preferences: Dict[str, Any] = {}
    accessibility_preferences: Dict[str, Any] = {}
    current_mastery_snapshot: Dict[str, Any] = {}
    learning_streak: int = 0
    total_questions_solved: int = 0
    current_diagnostic_score: float = 0.0
    current_recommendation_queue: List[str] = []


class TeacherProfileSchema(BaseModel):
    institution: Optional[str] = None
    department: Optional[str] = None
    subjects: List[str] = []
    assigned_classes: List[str] = []
    years_of_experience: int = 0
    verification_status: str = "pending"


class AdminProfileSchema(BaseModel):
    organization: Optional[str] = None
    permission_level: str = "super_admin"
    system_privileges: List[str] = []


class UserProfileResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    phone_number: Optional[str] = None
    profile_photo: Optional[str] = None
    role: str
    status: str
    email_verified: bool
    account_verified: bool
    timezone: str
    language: str
    theme_preference: str
    created_at: datetime
    last_login: Optional[datetime] = None
    student_profile: Optional[StudentProfileSchema] = None
    teacher_profile: Optional[TeacherProfileSchema] = None
    admin_profile: Optional[AdminProfileSchema] = None


class ProfileUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    timezone: Optional[str] = None
    language: Optional[str] = None
    student_profile: Optional[StudentProfileSchema] = None
    teacher_profile: Optional[TeacherProfileSchema] = None
    admin_profile: Optional[AdminProfileSchema] = None


class PreferencesUpdateRequest(BaseModel):
    theme: Optional[str] = "dark"
    language: Optional[str] = "en"
    notifications_enabled: Optional[Dict[str, bool]] = None


class SessionResponse(BaseModel):
    id: str
    device_info: Optional[str] = None
    ip_address: Optional[str] = None
    is_active: bool
    last_active_at: datetime
    created_at: datetime
