import os

from fastapi import FastAPI
from injector import Injector

from src.domain.configuration_env import ConfigurationEnv
from src.infrastructure.config import Configuration

config: ConfigurationEnv = Configuration(os.getenv("ENV", "dev")).get_config()


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()

    # print("Iniciando app...")
    # obj_dict = vars(config)

    # json_output = json.dumps(obj_dict, indent=4)
    # print(json_output)

    return app
