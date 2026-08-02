import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check_endpoint(async_client: AsyncClient):
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "data" in json_data
    assert json_data["data"]["version"] == "0.1.0"


@pytest.mark.asyncio
async def test_module_placeholders(async_client: AsyncClient):
    modules = [
        "/api/v1/auth/status",
        "/api/v1/knowledge-graph/status",
        "/api/v1/questions/status",
        "/api/v1/diagnostics/status",
        "/api/v1/mastery/status",
        "/api/v1/recommendations/status",
        "/api/v1/analytics/status",
        "/api/v1/teacher/status",
        "/api/v1/admin/status",
    ]

    for path in modules:
        res = await async_client.get(path)
        assert res.status_code == 200, f"Failed for path {path}"
        body = res.json()
        assert body["success"] is True
        assert body["code"] == "MODULE_INITIALIZED"
