from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar


Entity = TypeVar("Entity")


class IBaseRepository(ABC, Generic[Entity]):
    @abstractmethod
    def create(self, entity: Entity):
        """Create entity in DB"""

    @abstractmethod
    def create_list(self, entity_list: List[Entity]):
        """Create a list of entities in DB"""

    @abstractmethod
    def find_by_uid(self, uid: str) -> Entity:
        """Find Pokemon by uid"""

    @abstractmethod
    def get_all(self) -> Entity:
        """get all data ok pokemon"""

    @abstractmethod
    def update(self, update_entity: Entity) -> None:
        """Update an object"""

    @abstractmethod
    def update_range(self, update_entity: List[Entity]) -> None:
        """Update a list of objects"""

    @abstractmethod
    def delete_by_uid(self, uid: str) -> None:
        """Delete by uid"""

    @abstractmethod
    def delete_range(self, uid: List[str]) -> None:
        """Delete range of uid"""
