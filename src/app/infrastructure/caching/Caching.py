from abc import ABC, abstractmethod
from typing import Optional, Any


class BaseCaching(ABC):
    @abstractmethod
    async def get(self, id: int) -> Optional[Any]:
        NotImplementedError()

    @abstractmethod
    async def set(self, value) -> None:
        NotImplementedError()
