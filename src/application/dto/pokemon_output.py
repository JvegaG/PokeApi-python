from dataclasses import dataclass
from datetime import datetime


@dataclass
class PokemonOutputDto:
    uid: str
    app_creation_date: datetime
    name: str
    base_experience: int
    locationarea_encounters: str
    weight: int
    height: int
