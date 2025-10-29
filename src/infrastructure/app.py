import os

from fastapi import FastAPI
from injector import Injector, SingletonScope
from fastapi_injector import attach_injector


from adapter.Controllers import abilityController, pokemonController
from src.domain.configuration_env import ConfigurationEnv
from src.infrastructure.config import Configuration

config: ConfigurationEnv = Configuration(os.getenv("ENV", "dev")).get_config()

api_version = "v1"


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()

    # print("Iniciando app...")
    # obj_dict = vars(config)

    # json_output = json.dumps(obj_dict, indent=4)
    # print(json_output)
    app.include_router(
        abilityController.router,
        prefix="api/{}/ability".format(api_version),
        tags=["ability"],
    )
    app.include_router(
        pokemonController.router,
        prefix="api/{}/pokemon".format(api_version),
        tags=["pokemon"],
    )
    injector.binder.bind(
        RepositoriesFactory, to=repositories_factory, scope=SingletonScope
    )

    attach_injector(app, injector)
    return app
