from abc import abstractmethod
from dataclasses import dataclass

from application.interfaces.repositories.base_repository import IBaseRepository
from domain.entities.pokemon import Pokemon


@dataclass
class IPokemonRepository(IBaseRepository):
    """Pokemon Reposity interface"""

    @abstractmethod
    def find_by_name(self, name: str) -> Pokemon:
        """Find Pokemon by name"""
