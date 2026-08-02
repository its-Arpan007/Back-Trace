import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_questions_api(async_client: AsyncClient):
    res = await async_client.get("/api/v1/questions")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True


@pytest.mark.asyncio
async def test_practice_set_api(async_client: AsyncClient):
    req_body = {
        "concept_codes": ["DSA_ARRAYS_01"],
        "difficulty": "medium",
        "question_count": 3,
        "adaptive": True,
    }
    res = await async_client.post("/api/v1/questions/practice-set", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "questions" in data["data"]
