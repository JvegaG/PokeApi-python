class SpeciePresenter:
    def __init__(
        self,
        uid: str,
        app_created_by: str,
        app_creation_date: str,
        app_last_update_by: str,
        app_last_update_date: str,
        name: str,
        url: str,
    ):
        self.uid = uid
        self.app_created_by = app_created_by
        self.app_creation_date = app_creation_date
        self.app_last_update_by = app_last_update_by
        self.app_last_update_date = app_last_update_date
        self.name = name
        self.url = url
