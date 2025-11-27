from dataclasses import dataclass

from domain.entities.base_entity import BaseEntity
from domain.entities.specie import Specie


@dataclass
class Ability(BaseEntity):
    specie: Specie
    is_hidden: bool
    slot: int
