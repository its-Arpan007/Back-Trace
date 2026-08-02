import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.admin import (
    AdminDashboardSummaryDTO,
    UserAdminDTO,
    SystemHealthDTO,
    AIConfigDTO,
    AuditLogItemDTO,
    ApprovalItemDTO,
)
from app.services.admin_service import AdminService

router = APIRouter(prefix="/admin", tags=["Administrator & Content Management Platform"])


@router.get("/dashboard", response_model=BaseResponse[AdminDashboardSummaryDTO])
async def get_admin_dashboard(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[AdminDashboardSummaryDTO]:
    service = AdminService(db)
    dto = await service.get_dashboard_summary()
    return BaseResponse(
        success=True,
        message="Enterprise admin dashboard metrics retrieved",
        code="ADMIN_DASHBOARD_RETRIEVED",
        data=dto,
    )


@router.get("/users", response_model=BaseResponse[List[UserAdminDTO]])
async def get_all_users(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[UserAdminDTO]]:
    service = AdminService(db)
    dtos = await service.get_users()
    return BaseResponse(
        success=True,
        message="Platform users retrieved",
        code="ADMIN_USERS_RETRIEVED",
        data=dtos,
    )


@router.get("/system-health", response_model=BaseResponse[SystemHealthDTO])
async def get_system_health(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[SystemHealthDTO]:
    service = AdminService(db)
    dto = await service.get_system_health()
    return BaseResponse(
        success=True,
        message="System monitoring status operational",
        code="SYSTEM_HEALTH_RETRIEVED",
        data=dto,
    )


@router.get("/ai-config", response_model=BaseResponse[AIConfigDTO])
async def get_ai_config(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[AIConfigDTO]:
    service = AdminService(db)
    dto = await service.get_ai_config()
    return BaseResponse(
        success=True,
        message="AI feature flags and prompt configuration retrieved",
        code="AI_CONFIG_RETRIEVED",
        data=dto,
    )


@router.get("/audit-logs", response_model=BaseResponse[List[AuditLogItemDTO]])
async def get_audit_logs(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[AuditLogItemDTO]]:
    service = AdminService(db)
    dtos = await service.get_audit_logs()
    return BaseResponse(
        success=True,
        message="System audit logs retrieved",
        code="AUDIT_LOGS_RETRIEVED",
        data=dtos,
    )


@router.get("/approvals", response_model=BaseResponse[List[ApprovalItemDTO]])
async def get_pending_approvals(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[ApprovalItemDTO]]:
    service = AdminService(db)
    dtos = await service.get_pending_approvals()
    return BaseResponse(
        success=True,
        message="Pending approval queue retrieved",
        code="APPROVALS_RETRIEVED",
        data=dtos,
    )


@router.post("/backups", response_model=BaseResponse[Dict[str, Any]])
async def trigger_backup_endpoint(
    db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = AdminService(db)
    res = await service.trigger_backup()
    return BaseResponse(
        success=True,
        message="Manual enterprise system backup executed successfully",
        code="BACKUP_EXECUTED",
        data=res,
    )
