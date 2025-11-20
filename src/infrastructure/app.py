import os

from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector

from infrastructure.error.api_exception import ApiException
from infrastructure.error.error_handler import (
    api_exception_handler,
    general_exception_handler,
)
from interfaces.api.controllers import abilityController, pokemonController
from infrastructure.config.config import Configuration
from infrastructure.config.configuration_env import ConfigurationEnv

config: ConfigurationEnv = Configuration(os.getenv("ENV", "dev")).get_config()

api_version = "v1"


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI(title=config.Project_name)

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
    # injector.binder.bind(
    #     RepositoriesFactory, to=repositories_factory, scope=SingletonScope
    # )

    attach_injector(app, injector)
    return app
