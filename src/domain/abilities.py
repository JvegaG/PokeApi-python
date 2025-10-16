from species import Species
from base_entity import BaseEntity


class Abilities(BaseEntity):
    def __init__(self, ability: Species, is_hidden: bool, slot: int):
        super().__init__()
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot
