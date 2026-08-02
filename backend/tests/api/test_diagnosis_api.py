import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_diagnosis_analyze_api(async_client: AsyncClient):
    req_body = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "question_id": "q1_arrays_01",
        "student_answer": "0x1005",
        "time_spent_seconds": 45,
        "hints_used": 1,
    }
    res = await async_client.post("/api/v1/diagnosis/analyze", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["processing_time_ms"] < 300.0


@pytest.mark.asyncio
async def test_diagnosis_explain_api(async_client: AsyncClient):
    req_body = {"diagnosis_id": "11111111-1111-1111-1111-111111111111"}
    res = await async_client.post("/api/v1/diagnosis/explain", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "natural_language_explanation" in data["data"]
