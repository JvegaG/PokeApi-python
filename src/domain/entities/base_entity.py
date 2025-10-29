from datetime import datetime


class BaseEntity:
    def __init__(
        self,
        uid: str,
        app_created_by: str,
        app_creation_date: datetime,
        app_last_update_by: str,
        app_last_update_date: datetime,
    ) -> None:
        self.Uid = uid
        self.AppCreatedBy = app_created_by
        self.AppCreationDate = app_creation_date
        self.AppLastUpdateBy = app_last_update_by
        self.AppLastUpdateDate = app_last_update_date

    pass
