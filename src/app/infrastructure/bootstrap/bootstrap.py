from app.utils.ioc import ioc
from app.infrastructure.bootstrap.config import get_config
from app.infrastructure.config import RootConfig

from app.infrastructure.caching import UserCaching, create_session


async def init_app(
    app_config_path: str = "./configs/app.yaml",
    webhook_config_path: str = "./configs/webhook.yaml",
    telegram_config_path: str = "./configs/telegram.yaml",
    database_config_path: str = "./configs/mysql.yaml",
) -> None:
    config = get_config(
        app_config_path=app_config_path,
        webhook_config_path=webhook_config_path,
        telegram_config_path=telegram_config_path,
        database_config_path=database_config_path,
    )

    if config.redis:
        user_caching = UserCaching(
            session=await create_session(config.redis)
        )
        ioc.set(UserCaching, user_caching)

    # Store in IOC
    ioc.set(RootConfig, config)
