from dataclasses import dataclass
from datetime import datetime

from application.dto.specie_output_dto import SpecieOutputDto


@dataclass
class AbilityOutputDto:
    uid: str
    specie: SpecieOutputDto
    app_creation_date: datetime
    is_hidden: bool
    slot: int
