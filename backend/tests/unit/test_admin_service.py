import pytest
from app.services.admin_service import AdminService


@pytest.mark.asyncio
async def test_admin_dashboard_summary():
    service = AdminService(None)
    summary = await service.get_dashboard_summary()
    assert summary.system_status == "healthy"
    assert summary.active_users_count == 150


@pytest.mark.asyncio
async def test_admin_trigger_backup():
    service = AdminService(None)
    res = await service.trigger_backup()
    assert res["status"] == "completed"
    assert res["size_mb"] > 0
