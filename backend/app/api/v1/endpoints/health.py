from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database.session import get_db
from app.services.redis import redis_service
from app.schemas.health import HealthCheckResponse
from app.schemas.base import BaseResponse
from app.core.config import settings

router = APIRouter(prefix="/health", tags=["Health & Diagnostics"])


@router.get("", response_model=BaseResponse[HealthCheckResponse])
async def health_check(db: AsyncSession = Depends(get_db)) -> BaseResponse[HealthCheckResponse]:
    """Diagnostic health check verifying DB and Redis connectivity."""
    db_connected = False
    try:
        await db.execute(text("SELECT 1"))
        db_connected = True
    except Exception:
        db_connected = False

    redis_connected = await redis_service.is_healthy()

    status_str = "healthy" if (db_connected and redis_connected) else "degraded"

    health_data = HealthCheckResponse(
        status=status_str,
        environment=settings.ENVIRONMENT,
        version=settings.VERSION,
        database_connected=db_connected,
        redis_connected=redis_connected,
        details={
            "platform": settings.PROJECT_NAME,
            "database_engine": "PostgreSQL (asyncpg)",
            "cache_engine": "Redis",
        },
    )

    return BaseResponse(
        success=True,
        message=f"BACKTRACE system status: {status_str.upper()}",
        code="HEALTH_OK" if status_str == "healthy" else "HEALTH_DEGRADED",
        data=health_data,
    )
