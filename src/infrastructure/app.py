import os

from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector

from infrastructure.database.database import init_db
from infrastructure.error.api_exception import ApiException
from infrastructure.error.error_handler import (
    api_exception_handler,
    general_exception_handler,
)
from infrastructure.config.config import Configuration
from infrastructure.config.configuration_env import ConfigurationEnv
from interface_adapters.api.controllers import abilityController, pokemonController

config: ConfigurationEnv = Configuration(os.getenv("ENV", "dev")).get_config()

api_version = "v1"


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI(title=config.project_name)
    init_db()
    # print("Iniciando app...")
    # obj_dict = vars(config)

    # json_output = json.dumps(obj_dict, indent=4)
    # print(json_output)

    app.add_exception_handler(ApiException, api_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)

    app.include_router(
        abilityController.router,
        prefix="/api/{}/ability".format(api_version),
        tags=["ability"],
    )
    app.include_router(
        pokemonController.router,
        prefix="/api/{}/pokemon".format(api_version),
        tags=["pokemon"],
    )

    attach_injector(app, injector)
    return app
