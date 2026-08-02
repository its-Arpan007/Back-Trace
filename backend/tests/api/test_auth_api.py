import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_auth_me_unauthorized(async_client: AsyncClient):
    res = await async_client.get("/api/v1/auth/me")
    assert res.status_code == 401


@pytest.mark.asyncio
async def test_profile_unauthorized(async_client: AsyncClient):
    res = await async_client.get("/api/v1/profile")
    assert res.status_code == 401
