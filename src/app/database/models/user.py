from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
import datetime

from .dataclasses import UserType


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    type = Column(String(32), default=UserType.USER)
    user_id = Column(BigInteger, unique=True)
    fullname = Column(String(128))
    username = Column(String(32), nullable=True)
    register_at = Column(DateTime, default=datetime.datetime.now)

    @property
    def is_admin(self) -> bool:
        return self.type == UserType.ADMIN
    
    def to_object(self) -> object:
        return {
            "id": self.id,
            "type": self.type,
            "user_id": self.user_id,
            "fullname": self.fullname,
            "username": self.username,
            "register_at": self.register_at,
        }
    
    def __repr__(self) -> str:
        return f"<{self.id}> [{self.user_id}] @{self.username} is {self.type} / register at: {self.register_at}"
