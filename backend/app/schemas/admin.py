from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AdminDashboardSummaryDTO(BaseModel):
    system_status: str = "healthy"
    active_users_count: int = 150
    daily_diagnoses_count: int = 42
    learning_sessions_count: int = 85
    recommendation_acceptance_pct: float = 88.5
    api_health_pct: float = 99.9
    database_status: str = "connected"
    storage_used_gb: float = 12.4
    pending_approvals_count: int = 3


class UserAdminDTO(BaseModel):
    user_id: str
    full_name: str
    email: str
    role: str # student, teacher, admin
    is_active: bool = True
    created_at: str


class SystemHealthDTO(BaseModel):
    api_status: str = "operational"
    database_latency_ms: float = 4.2
    redis_status: str = "healthy"
    background_jobs_queue_size: int = 0
    event_bus_status: str = "active"
    error_rate_pct: float = 0.01


class AIConfigDTO(BaseModel):
    model_version: str = "gemini-1.5-pro"
    feature_flags: Dict[str, bool] = Field(default_factory=lambda: {"adaptive_practice": True, "ai_explanation": True})
    prompt_templates: Dict[str, str] = Field(default_factory=dict)
    safety_rules_count: int = 12


class AuditLogItemDTO(BaseModel):
    log_id: str
    timestamp: str
    user_id: str
    action: str
    resource: str
    ip_address: str = "127.0.0.1"


class ApprovalItemDTO(BaseModel):
    approval_id: str
    item_type: str # curriculum, question, resource, graph
    title: str
    requested_by: str
    created_at: str
