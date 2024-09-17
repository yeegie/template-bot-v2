from app.adapters.SessionCreator import BaseSessionCreator
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.config import MysqlDatabase


class SqlalchemySessionCreator(BaseSessionCreator):
    def __init__(self, database_config: MysqlDatabase) -> None:
        self._db_uri = self.__build_connection_string()
        self._engine = create_async_engine(self._db_uri, echo=True)
        
        self._SessionLocal = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    def __build_connection_string(self) -> str:
        return (
            f"{self.__config.db_type}://{self.__config.user}:"
            f"{self.__config.password}@{self.__config.host}:"
            f"{self.__config.port}/{self.__config.database}"
        )
    
    def create_session(self) -> AsyncSession:
        return self._SessionLocal()
