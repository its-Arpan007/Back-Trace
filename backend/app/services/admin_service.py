import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.admin import (
    AdminDashboardSummaryDTO,
    UserAdminDTO,
    SystemHealthDTO,
    AIConfigDTO,
    AuditLogItemDTO,
    ApprovalItemDTO,
)


class AdminService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_dashboard_summary(self) -> AdminDashboardSummaryDTO:
        return AdminDashboardSummaryDTO()

    async def get_users(self) -> List[UserAdminDTO]:
        return [
            UserAdminDTO(user_id="11111111-1111-1111-1111-111111111111", full_name="Alex Rivera", email="alex@backtrace.ai", role="student", is_active=True, created_at="2026-08-01"),
            UserAdminDTO(user_id="22222222-2222-2222-2222-222222222222", full_name="Dr. Smith", email="smith@backtrace.ai", role="teacher", is_active=True, created_at="2026-08-01"),
            UserAdminDTO(user_id="33333333-3333-3333-3333-333333333333", full_name="System Administrator", email="admin@backtrace.ai", role="admin", is_active=True, created_at="2026-08-01"),
        ]

    async def get_system_health(self) -> SystemHealthDTO:
        return SystemHealthDTO()

    async def get_ai_config(self) -> AIConfigDTO:
        return AIConfigDTO(
            model_version="gemini-1.5-pro",
            feature_flags={"adaptive_practice": True, "ai_explanation": True, "decay_recovery": True},
            prompt_templates={"reflection_prompt": "Reflect on your memory layout calculation error..."},
            safety_rules_count=12,
        )

    async def get_audit_logs(self) -> List[AuditLogItemDTO]:
        return [
            AuditLogItemDTO(log_id="log_01", timestamp=datetime.now(timezone.utc).isoformat(), user_id="33333333-3333-3333-3333-333333333333", action="UPDATE_AI_CONFIG", resource="prompt_templates"),
            AuditLogItemDTO(log_id="log_02", timestamp=datetime.now(timezone.utc).isoformat(), user_id="33333333-3333-3333-3333-333333333333", action="APPROVE_QUESTION", resource="q1_arrays_01"),
        ]

    async def get_pending_approvals(self) -> List[ApprovalItemDTO]:
        return [
            ApprovalItemDTO(approval_id="app_01", item_type="question", title="Array Offset Multiplication Question", requested_by="Dr. Smith", created_at="2026-08-02"),
            ApprovalItemDTO(approval_id="app_02", item_type="graph", title="Add Prerequisite Link: DSA_COMPARISONS_01 -> DSA_ARRAYS_01", requested_by="Dr. Smith", created_at="2026-08-02"),
        ]

    async def trigger_backup(self) -> Dict[str, Any]:
        return {
            "backup_id": str(uuid.uuid4()),
            "status": "completed",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "size_mb": 142.5,
        }
