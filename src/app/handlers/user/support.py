from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from app.utils.ioc import ioc
from app.infrastructure.config import RootConfig

from app.handlers.routers import user_router


@user_router.message(Command(commands=["support", "help"]))
async def welcome(message: Message, state: FSMContext):
    support = ioc.get(RootConfig).telegram.support
    await message.answer(f"📞 For any questions: @{support}")
