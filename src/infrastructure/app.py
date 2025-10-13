from fastapi import FastAPI
from injector import Injector


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()

    return app
