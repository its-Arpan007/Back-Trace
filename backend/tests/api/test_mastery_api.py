import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_student_mastery_summary_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/mastery/student/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "concept_masteries" in data["data"]


@pytest.mark.asyncio
async def test_get_mastery_timeline_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/mastery/timeline/{student_id}?concept_code=DSA_ARRAYS_01")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert len(data["data"]["timeline"]) > 0


@pytest.mark.asyncio
async def test_recalculate_mastery_api(async_client: AsyncClient):
    req_body = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "concept_code": "DSA_ARRAYS_01",
    }
    res = await async_client.post("/api/v1/mastery/recalculate", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
