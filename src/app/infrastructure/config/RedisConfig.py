__all__ = [
    "RedisConfig"
]

from pydantic import BaseModel, SecretStr
from typing import Optional


class RedisConfig(BaseModel):
    host: str
    port: int
    db: Optional[int] = None
    password: Optional[SecretStr] = None
