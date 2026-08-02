from datetime import datetime, timezone
import uuid
from sqlalchemy import DateTime, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Base declarative class for all SQLAlchemy models in BACKTRACE."""

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Automatically generate __tablename__ from class name in snake_case."""
        name = cls.__name__
        return "".join(
            ["_" + c.lower() if c.isupper() else c.lower() for c in name]
        ).lstrip("_")


class UUIDPrimaryKeyMixin:
    """Mixin for models requiring a UUID primary key."""

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )


class TimestampMixin:
    """Mixin for models tracking created_at and updated_at timestamps."""

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
