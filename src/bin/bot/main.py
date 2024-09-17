import asyncio

from app.infrastructure.bootstrap import init_app
from app.utils.ioc import ioc

from app.infrastructure.config import RootConfig

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

import app.handlers.routers as routers

from loguru import logger


async def on_startup(bot: Bot, dispatcher: Dispatcher):
    logger.info('[📦] Launching the bot...')
    
    config = ioc.get(RootConfig)

    # Webhook setup
    await bot.set_webhook(f'{config.webhook.base_url}{config.webhook.bot_path}')

    # Include routers
    dispatcher.include_router(routers.user_router)
    dispatcher.include_router(routers.admin_router)

    # Final log
    logger.info(f'[!] Bot stated -- @{(await bot.get_me()).username}')


async def on_shutdown(bot: Bot):
    logger.info('[X] Stopping bot...')
    await bot.delete_webhook()


def main():
    asyncio.run(init_app())

    config = ioc.get(RootConfig)

    properties = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )

    bot = Bot(
        token=config.telegram.token.get_secret_value(),
        default=properties,
    )

    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    app = web.Application()
    request_handler = SimpleRequestHandler(
        dispatcher,
        bot,
    )

    request_handler.register(app, path=config.webhook.bot_path)
    setup_application(app, dispatcher, bot=bot)

    web.run_app(app, host=config.webhook.listen_address, port=config.webhook.listen_port)


if __name__ == "__main__":
    main()
