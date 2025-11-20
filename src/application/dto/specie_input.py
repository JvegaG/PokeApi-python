from dataclasses import dataclass
from typing import Optional


@dataclass
class SpecieInputDto:
    name: str
    url: Optional[str]
