from domain.entities.base_entity import BaseEntity
from src.domain.entities.specie import Specie


class Ability(BaseEntity):
    def __init__(
        self,
        uid: str,
        app_created_by: str,
        app_creation_date: str,
        app_last_update_by: str,
        app_last_update_date: str,
        specie: Specie,
        is_hidden: bool,
        slot: int,
    ):
        super().__init__(
            uid,
            app_created_by,
            app_creation_date,
            app_last_update_by,
            app_last_update_date,
        )
        self.species = specie
        self.is_hidden = is_hidden
        self.slot = slot
