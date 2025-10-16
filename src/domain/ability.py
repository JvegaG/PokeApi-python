from src.domain.specie import Specie
from base_entity import BaseEntity


class Ability(BaseEntity):
    def __init__(self, specie: Specie, is_hidden: bool, slot: int):
        super().__init__()
        self.species = specie
        self.is_hidden = is_hidden
        self.slot = slot
