import sys
from pathlib import Path

import uvicorn
from injector import Injector

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from infrastructure.app import create_app

app = create_app(Injector())


if __name__ == "__main__":
    uvicorn.run("main:app")
