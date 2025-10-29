from datetime import datetime

from domain.entities.base_entity import BaseEntity


class Specie(BaseEntity):
    def __init__(
        self,
        uid: str,
        app_created_by: str,
        app_creation_date: datetime,
        app_last_update_by: str,
        app_last_update_date: datetime,
        name: str,
        url: str,
    ):
        super().__init__(
            uid,
            app_created_by,
            app_creation_date,
            app_last_update_by,
            app_last_update_date,
        )
        self.name = name
        self.url = url
