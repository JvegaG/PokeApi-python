from datetime import date


class BaseEntity:
    def __init__(
        self,
        Uid: str,
        AppCreatedBy: str,
        AppCreationDate: date,
        AppLastUpdateBy: str,
        AppLastUpdateDate: date,
    ) -> None:
        self.Uid = Uid
        self.AppCreatedBy = AppCreatedBy
        self.AppCreationDate = AppCreationDate
        self.AppLastUpdateBy = AppLastUpdateBy
        self.AppLastUpdateDate = AppLastUpdateDate

    pass
