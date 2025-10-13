from species import Species


class Habilities:
    def __init__(self, ability: Species, is_hidden: bool, slot: int):
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot
