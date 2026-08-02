import logging
from typing import Optional
import redis.asyncio as aioredis
from app.core.config import settings

logger = logging.getLogger("backtrace.redis")


class RedisService:
    def __init__(self) -> None:
        self.redis_client: Optional[aioredis.Redis] = None

    async def connect(self) -> None:
        """Establish async connection pool to Redis."""
        try:
            self.redis_client = aioredis.from_url(
                settings.REDIS_URL,
                decode_responses=True,
                socket_timeout=5,
            )
            await self.redis_client.ping()
            logger.info("Successfully connected to Redis instance.")
        except Exception as e:
            logger.warning(f"Failed to connect to Redis at {settings.REDIS_URL}: {e}")
            self.redis_client = None

    async def disconnect(self) -> None:
        """Close Redis connection pool."""
        if self.redis_client:
            await self.redis_client.close()
            logger.info("Closed Redis connection.")

    async def is_healthy(self) -> bool:
        """Check if Redis service responds to PING."""
        if not self.redis_client:
            return False
        try:
            return await self.redis_client.ping()
        except Exception:
            return False


redis_service = RedisService()
