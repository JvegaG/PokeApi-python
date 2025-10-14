class ConfigurationEnv:
    """Class containing environment variables."""

    def __init__(self, Postgres_db: str, PortDb: str, Database: str, env: str):
        self.Postgres_db = Postgres_db
        self.PortDb = PortDb
        self.Database = Database
        self.env = env
