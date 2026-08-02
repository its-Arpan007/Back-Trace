import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_student_analytics_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/analytics/student/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["student_id"] == student_id


@pytest.mark.asyncio
async def test_get_predictive_analytics_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/analytics/predictions/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "exam_readiness" in data["data"]


@pytest.mark.asyncio
async def test_get_performance_reports_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/analytics/reports/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["is_pdf_ready"] is True
