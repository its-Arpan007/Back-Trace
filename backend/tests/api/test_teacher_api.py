import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_teacher_classes_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/teacher/classes")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert len(data["data"]) > 0


@pytest.mark.asyncio
async def test_get_class_analytics_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/teacher/classes/c_dsa_101/analytics")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["class_id"] == "c_dsa_101"


@pytest.mark.asyncio
async def test_get_interventions_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/teacher/interventions")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert len(data["data"]) > 0
