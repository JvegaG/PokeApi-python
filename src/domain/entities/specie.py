from dataclasses import dataclass

from domain.entities.base_entity import BaseEntity


@dataclass
class Specie(BaseEntity):
    name: str
    url: str
