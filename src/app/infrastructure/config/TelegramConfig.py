__all__ = [
    "TelegramConfig"
]


from pydantic import BaseModel, SecretStr


class TelegramConfig(BaseModel):
    token: SecretStr
    support: str = "durov"
