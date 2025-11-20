from abc import ABC, abstractmethod

from application.dto.pokemon_output import PokemonOutputDto


class PokemonPresenter(ABC):
    @abstractmethod
    def present(self, pokemon_data: PokemonOutputDto) -> dict:
        pass
