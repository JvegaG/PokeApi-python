from dataclasses import dataclass


@dataclass
class ConfigurationEnv:
    project_name: str
    postgres_host: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: int
    env: str
