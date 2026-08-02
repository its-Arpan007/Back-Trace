import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_subjects(async_client: AsyncClient):
    res = await async_client.get("/api/v1/subjects")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True


@pytest.mark.asyncio
async def test_get_graph(async_client: AsyncClient):
    res = await async_client.get("/api/v1/graph")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "topological_order" in data["data"]


@pytest.mark.asyncio
async def test_get_dependencies(async_client: AsyncClient):
    res = await async_client.get("/api/v1/graph/dependencies/DSA_GRAPH_01")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "ancestors" in data["data"]
