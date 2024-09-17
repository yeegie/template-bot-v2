import redis.asyncio as redis
import asyncio

from app.infrastructure.config import RedisConfig


async def create_session(redis_config: RedisConfig) -> redis.Redis:
    session = redis.Redis(
        host=redis_config.host,
        port=redis_config.port,
        db=redis_config.db,
        password=redis_config.password.get_secret_value(),
        decode_responses=True,
    )

    await session.ping()
    return session
