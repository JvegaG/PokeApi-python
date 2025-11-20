from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

from application.interfaces.repositories.base_repository import BaseRepository
from domain.entities.pokemon import Pokemon


@dataclass
class PokemonRepository(BaseRepository[Pokemon]):

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[Pokemon]:
        pass
