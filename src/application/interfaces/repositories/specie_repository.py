from abc import abstractmethod
from typing import Optional
from application.interfaces.repositories.base_repository import BaseRepository
from domain.entities.specie import Specie


class SpecieRepository(BaseRepository[Specie]):

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[Specie]:
        pass
