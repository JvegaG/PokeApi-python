from typing import Optional
from domain.entities.pokemon import Pokemon
from infrastructure.database.model.pokemon import PokemonModel


class PokemonMapperDB:
    @staticmethod
    def _to_model(entity: Pokemon) -> PokemonModel:
        return PokemonModel(
            uid=entity.uid,
            name=entity.name,
            base_experience=entity.base_experience,
            locationarea_encounters=entity.locationarea_encounters,
            weight=entity.weight,
            height=entity.height,
            app_created_by=entity.app_created_by,
            app_creation_date=entity.app_creation_date,
            app_last_update_by=entity.app_last_update_by,
            app_last_update_date=entity.app_last_update_date,
        )

    @staticmethod
    def _to_entity(model: PokemonModel) -> Optional[Pokemon]:
        if not model:
            return None
        return Pokemon(
            uid=model.uid,
            name=model.name,
            base_experience=model.base_experience,
            locationarea_encounters=model.locationarea_encounters,
            weight=model.weight,
            height=model.height,
            app_created_by=model.app_created_by,
            app_creation_date=model.app_creation_date,
            app_last_update_by=model.app_last_update_by,
            app_last_update_date=model.app_last_update_date,
        )
