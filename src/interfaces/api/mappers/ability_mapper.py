from typing import Any

from application.mappers.api_mapper import ApiMapper
from domain.entities.ability import Ability
from interfaces.api.presenters.abilities_presenter import AbilityPresenter


class AbilityMapper(ApiMapper):
    def to_api(self, entity: Ability) -> AbilityPresenter:
        return AbilityPresenter(entity)

    def to_entity(self, payload: Any) -> Ability:
        return Ability(payload)
