from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

Entity = TypeVar("Entity")


class BaseRepository(ABC, Generic[Entity]):
    @abstractmethod
    async def create(self, entity: Entity):
        pass

    @abstractmethod
    async def create_list(self, entity_list: List[Entity]):
        pass

    @abstractmethod
    async def find_by_uid(self, uid: str) -> Optional[Entity]:
        pass

    @abstractmethod
    async def get_all(self) -> List[Entity]:
        pass

    @abstractmethod
    async def update(self, update_entity: Entity) -> None:
        pass

    @abstractmethod
    async def update_range(self, update_entity: List[Entity]) -> None:
        pass

    @abstractmethod
    async def delete_by_uid(self, uid: str) -> None:
        pass

    @abstractmethod
    async def delete_range(self, uid: List[str]) -> None:
        pass
