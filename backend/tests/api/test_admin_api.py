import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_admin_dashboard_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/admin/dashboard")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["system_status"] == "healthy"


@pytest.mark.asyncio
async def test_get_system_health_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/admin/system-health")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["api_status"] == "operational"


@pytest.mark.asyncio
async def test_trigger_backup_api(async_client: AsyncClient):
    res = await async_client.post("/api/v1/admin/backups")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["status"] == "completed"
