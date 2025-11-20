from dataclasses import dataclass
from datetime import datetime, timezone
import uuid

from domain.entities.base_entity import BaseEntity


@dataclass
class Pokemon(BaseEntity):
    name: str
    base_experience: int
    locationarea_encounters: str
    weight: int
    height: int

    @classmethod
    def create(
        cls,
        name: str,
        base_experience: int,
        locationarea_encounters: str,
        weight: int,
        height: int,
    ) -> "Pokemon":
        """Factory method para crear usuario"""

        return cls(
            uid=str(uuid.uuid4()),
            name=name,
            base_experience=base_experience,
            locationarea_encounters=locationarea_encounters,
            weight=weight,
            height=height,
            app_created_by="system",
            app_creation_date=datetime.now(tz=timezone.utc),
            app_last_update_by="system",
            app_last_update_date=datetime.now(tz=timezone.utc),
        )
