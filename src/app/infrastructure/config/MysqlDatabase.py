__all__ = [
    "MysqlDatabase"
]


from pydantic import BaseModel, SecretStr


class MysqlDatabase(BaseModel):
    host: str = "localhost"
    port: int = 3306
    user: str
    password: SecretStr
    database: str
