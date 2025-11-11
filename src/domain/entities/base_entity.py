from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEntity:
    uid: str
    app_created_by: str
    app_creation_date: datetime
    app_last_update_by: str
    app_last_update_date: datetime
