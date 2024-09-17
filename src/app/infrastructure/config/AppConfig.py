__all__ = [
    "AppConfig"
]


from pydantic import BaseModel


class AppConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000
    debug: bool = False
