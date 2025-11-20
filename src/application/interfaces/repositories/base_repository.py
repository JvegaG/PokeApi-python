from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

Entity = TypeVar("Entity")


class BaseRepository(ABC, Generic[Entity]):
    @abstractmethod
    async def create(self, entity: Entity):
        """Create entity in DB"""
        pass

    @abstractmethod
    async def create_list(self, entity_list: List[Entity]):
        """Create a list of entities in DB"""
        pass

    @abstractmethod
    async def find_by_uid(self, uid: str) -> Optional[Entity]:
        """Find Pokemon by uid"""
        pass

    @abstractmethod
    async def get_all(self) -> List[Entity]:
        """get all data ok pokemon"""
        pass

    @abstractmethod
    async def update(self, update_entity: Entity) -> None:
        """Update an object"""
        pass

    @abstractmethod
    async def update_range(self, update_entity: List[Entity]) -> None:
        """Update a list of objects"""
        pass

    @abstractmethod
    async def delete_by_uid(self, uid: str) -> None:
        """Delete by uid"""
        pass

    @abstractmethod
    async def delete_range(self, uid: List[str]) -> None:
        """Delete range of uid"""
        pass
