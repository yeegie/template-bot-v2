__all__ = [
    "AppConfig"
]


from pydantic import BaseModel

from typing import Optional

from .AppConfig import AppConfig
from .WebhookConfig import WebhookConfig
from .TelegramConfig import TelegramConfig
from .MysqlDatabase import MysqlDatabase
from .RedisConfig import RedisConfig


class RootConfig(BaseModel):
    app: AppConfig
    webhook: WebhookConfig
    telegram: TelegramConfig
    databases: MysqlDatabase
    redis: Optional[RedisConfig] = None
