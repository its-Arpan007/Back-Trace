from datetime import datetime, timezone
import uuid
from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime,
    Integer,
    Float,
    ForeignKey,
    JSON,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class UserModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "users"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(50), nullable=True)
    profile_photo = Column(Text, nullable=True)
    role = Column(String(50), nullable=False, default="student", index=True)
    status = Column(String(50), nullable=False, default="active")
    email_verified = Column(Boolean, default=False, nullable=False)
    account_verified = Column(Boolean, default=False, nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
    timezone = Column(String(50), default="UTC", nullable=False)
    language = Column(String(10), default="en", nullable=False)
    theme_preference = Column(String(20), default="dark", nullable=False)

    # Relationships
    student_profile = relationship("StudentProfileModel", back_populates="user", uselist=False, cascade="all, delete-orphan")
    teacher_profile = relationship("TeacherProfileModel", back_populates="user", uselist=False, cascade="all, delete-orphan")
    admin_profile = relationship("AdminProfileModel", back_populates="user", uselist=False, cascade="all, delete-orphan")
    sessions = relationship("SessionModel", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLogModel", back_populates="user", cascade="all, delete-orphan")
    preferences = relationship("UserPreferencesModel", back_populates="user", uselist=False, cascade="all, delete-orphan")


class StudentProfileModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "student_profiles"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    education_level = Column(String(100), nullable=True)
    institution = Column(String(255), nullable=True)
    course = Column(String(100), nullable=True)
    semester = Column(Integer, nullable=True)
    subjects = Column(JSON, default=list, nullable=False)
    learning_preferences = Column(JSON, default=dict, nullable=False)
    accessibility_preferences = Column(JSON, default=dict, nullable=False)
    current_mastery_snapshot = Column(JSON, default=dict, nullable=False)
    learning_streak = Column(Integer, default=0, nullable=False)
    total_questions_solved = Column(Integer, default=0, nullable=False)
    current_diagnostic_score = Column(Float, default=0.0, nullable=False)
    current_recommendation_queue = Column(JSON, default=list, nullable=False)

    user = relationship("UserModel", back_populates="student_profile")


class TeacherProfileModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "teacher_profiles"

    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    institution = Column(String(255), nullable=True)
    department = Column(String(100), nullable=True)
    subjects = Column(JSON, default=list, nullable=False)
    assigned_classes = Column(JSON, default=list, nullable=False)
    years_of_experience = Column(Integer, default=0, nullable=False)
    verification_status = Column(String(50), default="pending", nullable=False)

    user = relationship("UserModel", back_populates="teacher_profile")


class AdminProfileModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "admin_profiles"

    admin_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    organization = Column(String(255), nullable=True)
    permission_level = Column(String(50), default="super_admin", nullable=False)
    system_privileges = Column(JSON, default=list, nullable=False)

    user = relationship("UserModel", back_populates="admin_profile")


class SessionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "sessions"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    device_info = Column(String(255), nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    last_active_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)

    user = relationship("UserModel", back_populates="sessions")
    refresh_tokens = relationship("RefreshTokenModel", back_populates="session", cascade="all, delete-orphan")


class RefreshTokenModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "refresh_tokens"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    token_hash = Column(String(255), unique=True, index=True, nullable=False)
    is_revoked = Column(Boolean, default=False, nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)

    session = relationship("SessionModel", back_populates="refresh_tokens")


class AuditLogModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "audit_logs"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    action = Column(String(100), nullable=False, index=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(Text, nullable=True)
    details = Column(JSON, default=dict, nullable=False)

    user = relationship("UserModel", back_populates="audit_logs")


class UserPreferencesModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "user_preferences"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    theme = Column(String(20), default="dark", nullable=False)
    language = Column(String(10), default="en", nullable=False)
    notifications_enabled = Column(JSON, default=dict, nullable=False)

    user = relationship("UserModel", back_populates="preferences")
