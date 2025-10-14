from injector import Injector
import uvicorn

from src.infrastructure.app import create_app

app = create_app(Injector())


# app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
