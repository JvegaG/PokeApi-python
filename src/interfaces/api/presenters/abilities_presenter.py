from dataclasses import dataclass
from datetime import datetime

from interfaces.api.presenters.species_presenter import SpeciePresenter


@dataclass
class AbilityPresenter:
    uid: str
    app_created_by: str
    app_creation_date: datetime
    app_last_update_by: str
    app_last_update_date: datetime
    specie: SpeciePresenter
    is_hidden: bool
    slot: int
