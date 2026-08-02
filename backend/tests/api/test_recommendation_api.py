import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_student_recommendations_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/recommendations/student/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert len(data["data"]) > 0


@pytest.mark.asyncio
async def test_get_todays_plan_api(async_client: AsyncClient):
    student_id = "11111111-1111-1111-1111-111111111111"
    res = await async_client.get(f"/api/v1/recommendations/today/{student_id}")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["plan_type"] == "today"


@pytest.mark.asyncio
async def test_recommendation_feedback_api(async_client: AsyncClient):
    req_body = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "recommendation_id": "11111111-1111-1111-1111-111111111111",
        "rating_score": 5,
        "feedback_text": "Extremely helpful interactive visualizer!",
        "action_taken": "accepted",
    }
    res = await async_client.post("/api/v1/recommendations/feedback", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
