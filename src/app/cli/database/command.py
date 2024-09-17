import asyncio
import click

from sqlalchemy.ext.asyncio import create_async_engine
from app.database.models.base import Base

# Models
from app.database.models import *

from app.infrastructure.config import MysqlDatabase


class DatabaseCommands:
    def __init__(self, config: MysqlDatabase) -> None:
        self.__config = config
        self.__connection_string = self.__build_connection_string()

    def __build_connection_string(self) -> str:
        return (
            f"mysql+aiomysql://{self.__config.user}:"
            f"{self.__config.password.get_secret_value()}@{self.__config.host}:"
            f"{self.__config.port}/{self.__config.database}"
        )
    
    def create_db(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__create())
        click.echo(f'[INFO] Database created.')

    async def __create(self):
        engine = create_async_engine(self.__connection_string, echo=True)
        
        # Create all tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        # Close engine
        await engine.dispose()
