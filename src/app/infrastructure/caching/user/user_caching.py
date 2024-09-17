from ..Caching import BaseCaching

import aioredis as redis
import json
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.models import User


class UserCaching(BaseCaching):
    def __init__(self, session: redis.Redis) -> None:
        self._session = session

    async def get(self, id: int) -> Optional[User]:
        cached_user = await self._session.get(id)

        if cached_user:
            return User(**json.loads(cached_user))
        
        return None

    async def set(self, user: User) -> None:
        await self._session.set(
            user.user_id, json.dumps(user.to_object())
        )
