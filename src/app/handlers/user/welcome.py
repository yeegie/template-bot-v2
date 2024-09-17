from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import random

from app.handlers.routers import user_router


@user_router.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    welcome_emoji = '🤖 👋 💎 🖖 🤙 👀 👻 👾'.split(' ')

    await state.clear()
    await message.answer(random.choice(welcome_emoji))
    await message.answer(f"Hello, {message.from_user.first_name} 👋")
