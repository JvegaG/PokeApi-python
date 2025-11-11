from dataclasses import asdict
from typing import Any

from application.mappers.api_mapper import ApiMapper
from domain.entities.pokemon import Pokemon
from interfaces.api.presenters.pokemon_presenter import PokemonPresenter


class PokemonMapper(ApiMapper):
    def to_api(self, entity: Pokemon) -> PokemonPresenter:
        return PokemonPresenter(**asdict(entity))

    def to_entity(self, payload: Any) -> Pokemon:
        return Pokemon(**asdict(payload))
