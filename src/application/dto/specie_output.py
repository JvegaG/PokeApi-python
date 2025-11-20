from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SpecieOutputDto:
    uid: str
    name: str
    app_creation_date: datetime
    url: Optional[str]
