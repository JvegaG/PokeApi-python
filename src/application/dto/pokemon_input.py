from dataclasses import dataclass
from typing import Optional


@dataclass
class PokemonInputDto:
    name: str
    base_experience: Optional[int]
    locationarea_encounters: Optional[str]
    weight: Optional[int]
    height: Optional[int]
