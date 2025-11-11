from dataclasses import asdict
from typing import Any

from application.mappers.api_mapper import ApiMapper
from domain.entities.specie import Specie
from interfaces.api.presenters.species_presenter import SpeciePresenter


class SpecieMapper(ApiMapper):
    def to_api(self, entity: Specie) -> SpeciePresenter:
        return SpeciePresenter(**asdict(entity))

    def to_entity(self, payload: Any) -> Specie:
        return Specie(**asdict(payload))
