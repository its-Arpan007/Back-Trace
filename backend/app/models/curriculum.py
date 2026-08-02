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


class SubjectModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "subjects"

    name = Column(String(100), nullable=False)
    code = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(String(100), default="book", nullable=False)
    color = Column(String(20), default="#14B8A6", nullable=False)
    difficulty_scale = Column(String(50), default="standard", nullable=False)
    status = Column(String(50), default="active", nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    chapters = relationship("ChapterModel", back_populates="subject", cascade="all, delete-orphan")


class ChapterModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "chapters"

    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, default=1, nullable=False)
    estimated_hours = Column(Float, default=1.0, nullable=False)
    difficulty = Column(String(50), default="medium", nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    subject = relationship("SubjectModel", back_populates="chapters")
    topics = relationship("TopicModel", back_populates="chapter", cascade="all, delete-orphan")


class TopicModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "topics"

    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, default=1, nullable=False)
    difficulty = Column(String(50), default="medium", nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    chapter = relationship("ChapterModel", back_populates="topics")
    concepts = relationship("ConceptModel", back_populates="topic", cascade="all, delete-orphan")


class ConceptModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concepts"

    topic_id = Column(UUID(as_uuid=True), ForeignKey("topics.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(String(50), default="medium", nullable=False)
    bloom_level = Column(String(50), default="apply", nullable=False)
    estimated_learning_time_minutes = Column(Integer, default=30, nullable=False)
    mastery_threshold = Column(Float, default=0.85, nullable=False)
    expected_accuracy = Column(Float, default=0.80, nullable=False)
    expected_confidence = Column(Float, default=0.75, nullable=False)
    learning_objective_count = Column(Integer, default=1, nullable=False)
    status = Column(String(50), default="active", nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    topic = relationship("TopicModel", back_populates="concepts")
    objectives = relationship("LearningObjectiveModel", back_populates="concept", cascade="all, delete-orphan")
    misconceptions = relationship("MisconceptionModel", back_populates="concept", cascade="all, delete-orphan")
    resources = relationship("ResourceModel", back_populates="concept", cascade="all, delete-orphan")
    aliases = relationship("ConceptAliasModel", back_populates="concept", cascade="all, delete-orphan")


class LearningObjectiveModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_objectives"

    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    objective = Column(Text, nullable=False)
    bloom_level = Column(String(50), default="apply", nullable=False)
    expected_outcome = Column(Text, nullable=True)
    success_criteria = Column(Text, nullable=True)

    concept = relationship("ConceptModel", back_populates="objectives")


class ConceptRelationshipModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concept_relationships"

    source_concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    target_concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    relationship_type = Column(String(50), default="Prerequisite", nullable=False) # Prerequisite, Depends On, Related, Extension, Alternative, Review, Advanced
    metadata_json = Column(JSON, default=dict, nullable=False)


class MisconceptionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "misconceptions"

    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    misconception_code = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(50), default="medium", nullable=False)
    common_student_mistakes = Column(JSON, default=list, nullable=False)
    detection_hints = Column(JSON, default=list, nullable=False)
    recommended_remediation = Column(JSON, default=list, nullable=False)

    concept = relationship("ConceptModel", back_populates="misconceptions")


class ResourceModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "resources"

    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    resource_type = Column(String(50), default="article", nullable=False) # article, video, interactive_lesson, book, pdf, external_link
    url = Column(Text, nullable=False)
    difficulty = Column(String(50), default="medium", nullable=False)
    duration_minutes = Column(Integer, default=10, nullable=False)
    language = Column(String(10), default="en", nullable=False)
    provider = Column(String(100), default="BACKTRACE", nullable=False)

    concept = relationship("ConceptModel", back_populates="resources")


class GraphNodeModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "graph_nodes"

    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), unique=True, nullable=False)
    node_label = Column(String(200), nullable=False)
    domain = Column(String(50), default="dsa", nullable=False, index=True)
    metadata_json = Column(JSON, default=dict, nullable=False)


class GraphEdgeModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "graph_edges"

    source_node_id = Column(UUID(as_uuid=True), ForeignKey("graph_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    target_node_id = Column(UUID(as_uuid=True), ForeignKey("graph_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    relationship_type = Column(String(50), default="PREREQUISITE_FOR", nullable=False)
    weight = Column(Float, default=1.0, nullable=False)


class LearningPathModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_paths"

    title = Column(String(200), nullable=False)
    domain = Column(String(50), nullable=False, index=True)
    concept_sequence = Column(JSON, default=list, nullable=False)
    path_type = Column(String(50), default="optimal", nullable=False) # optimal, remediation, revision


class ConceptAliasModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concept_aliases"

    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    alias_name = Column(String(150), index=True, nullable=False)

    concept = relationship("ConceptModel", back_populates="aliases")
