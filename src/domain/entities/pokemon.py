from dataclasses import dataclass

from domain.entities.base_entity import BaseEntity


@dataclass
class Pokemon(BaseEntity):
    name: str
    base_experience: int
    locationarea_encounters: str
    weight: int
    height: int
