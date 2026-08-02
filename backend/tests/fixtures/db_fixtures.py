import pytest
from typing import AsyncGenerator


@pytest.fixture
async def mock_db_session() -> AsyncGenerator[None, None]:
    """Fixture placeholder for DB session mocks."""
    yield
