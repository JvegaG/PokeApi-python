from dataclasses import dataclass


@dataclass
class ConfigurationEnv:
    Project_name: str
    Postgres_db: str
    PortDb: str
    Database: str
    env: str
