from typing import Dict, Optional
from dotenv import dotenv_values

from src.domain.configuration_env import ConfigurationEnv


class Configuration:
    def __init__(self, env: str) -> None:
        env = env.lower()

        __config_raw: Dict[str, Optional[str]] = dotenv_values(
            f".env.{env}".format(env)
        )

        postgres_db = __config_raw.get("POSTGRES_DB") or ""
        portDB = __config_raw.get("PORTDB") or ""
        database = __config_raw.get("DATABASE") or ""

        self.config = ConfigurationEnv(postgres_db, portDB, database, env)

    def get_config(self) -> ConfigurationEnv:
        return self.config
