from typing import Dict, Optional

from dotenv import dotenv_values

from infrastructure.config.configuration_env import ConfigurationEnv


class Configuration:
    def __init__(self, env: str) -> None:
        env = env.lower()

        __config_raw: Dict[str, Optional[str]] = dotenv_values(
            f".env.{env}".format(env)
        )

        project_name = __config_raw.get("PROJECT_NAME") or ""
        postgres_host = __config_raw.get("POSTGRES_HOST") or ""
        postgres_db = __config_raw.get("POSTGRES_DB") or ""
        postgres_user = __config_raw.get("POSTGRES_USER") or ""
        postgres_password = __config_raw.get("POSTGRES_PASSWORD") or ""
        port_db = __config_raw.get("POSTGRES_PORT") or ""
        env = __config_raw.get("ENV") or ""

        self.config = ConfigurationEnv(
            project_name,
            postgres_host,
            postgres_db,
            postgres_user,
            postgres_password,
            int(port_db),
            env,
        )

    def get_config(self) -> ConfigurationEnv:
        return self.config
