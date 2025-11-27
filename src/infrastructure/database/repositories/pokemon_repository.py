from typing import List, Optional

from sqlalchemy.orm import Session

from application.interfaces.repositories.pokemon_repository import IPokemonRepository
from domain.entities.pokemon import Pokemon
from infrastructure.database.mappers.pokemon_mapper_DB import PokemonMapperDB
from infrastructure.database.model.pokemon import PokemonModel


class PokemonRepository(IPokemonRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create(self, entity: Pokemon):
        model = PokemonMapperDB._to_model(entity)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

    async def create_list(self, entity_list: List[Pokemon]):
        models = [PokemonMapperDB._to_model(entity) for entity in entity_list]
        self.db.add_all(models)
        self.db.commit()

    async def find_by_uid(self, uid: str) -> Optional[Pokemon]:
        model = self.db.query(PokemonModel).filter(PokemonModel.uid == uid).first()
        return PokemonMapperDB._to_entity(model) if model else None

    async def get_all(self) -> List[Pokemon]:
        models = self.db.query(PokemonModel).all()
        entities = [PokemonMapperDB._to_entity(model) for model in models]
        return [entity for entity in entities if entity is not None]

    async def update(self, update_entity: Pokemon) -> None:
        model = (
            self.db.query(PokemonModel)
            .filter(PokemonModel.uid == update_entity.uid)
            .first()
        )
        if model:
            model.name = update_entity.name
            model.base_experience = update_entity.base_experience
            model.locationarea_encounters = update_entity.locationarea_encounters
            model.weight = update_entity.weight
            model.height = update_entity.height
            model.app_last_update_by = update_entity.app_last_update_by
            model.app_last_update_date = update_entity.app_last_update_date
            self.db.commit()

    async def update_range(self, update_entity: List[Pokemon]) -> None:
        for entity in update_entity:
            await self.update(entity)

    async def delete_by_uid(self, uid: str) -> None:
        model = self.db.query(PokemonModel).filter(PokemonModel.uid == uid).first()
        if model:
            self.db.delete(model)
            self.db.commit()

    async def delete_range(self, uids: List[str]) -> None:
        self.db.query(PokemonModel).filter(PokemonModel.uid.in_(uids)).delete(
            synchronize_session=False
        )
        self.db.commit()

    async def find_by_name(self, name: str) -> Optional[Pokemon]:
        model = self.db.query(PokemonModel).filter(PokemonModel.name == name).first()
        return PokemonMapperDB._to_entity(model) if model else None
