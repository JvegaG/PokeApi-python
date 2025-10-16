from base_entity import BaseEntity


class Species(BaseEntity):
    def __init__(self, name: str, url: str):
        super().__init__()
        self.name = name
        self.url = url
