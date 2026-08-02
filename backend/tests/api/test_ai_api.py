import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ai_chat_api(async_client: AsyncClient):
    req_body = {
        "user_id": "11111111-1111-1111-1111-111111111111",
        "message": "Why was my stride offset calculation wrong?",
        "concept_code": "DSA_ARRAYS_01",
        "provider": "gemini",
    }
    res = await async_client.post("/api/v1/ai/chat", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "reply" in data["data"]


@pytest.mark.asyncio
async def test_ai_explain_api(async_client: AsyncClient):
    req_body = {
        "concept_code": "DSA_ARRAYS_01",
        "explanation_type": "analogy",
    }
    res = await async_client.post("/api/v1/ai/explain", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "analogy" in data["data"]
