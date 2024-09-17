from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database.models import User


class ManageUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        session: AsyncSession = data['session']
        async with session.begin():
            # Find user by id
            query = select(User).where(User.user_id == event.from_user.id)
            result = await session.execute(query)
            user = result.scalars().first()

            is_bot = False
            if isinstance(event, Message):
                is_bot = event.from_user.is_bot
            elif isinstance(event, CallbackQuery):
                is_bot = event.message.from_user.is_bot

            if not is_bot:
                bot: Bot = data['bot']
                if user is None:
                    # New user
                    user = User(
                        user_id=event.from_user.id,
                        full_name=event.from_user.full_name,
                        username=event.from_user.username,
                        language=event.from_user.language_code,
                    )
                    session.add(user)
                else:
                    # Update info
                    if user.full_name != event.from_user.full_name or user.username != event.from_user.username:
                        user.full_name = event.from_user.full_name
                        user.username = event.from_user.username
                        session.add(user)

        data['user'] = user
        return await handler(event, data)