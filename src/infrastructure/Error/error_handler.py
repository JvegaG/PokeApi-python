import logging
import traceback
from typing import cast

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from infrastructure.Error.api_exception import ApiException

logger = logging.getLogger(__name__)


async def api_exception_handler(request: Request, exc: Exception):
    exc = cast(ApiException, exc)
    # Capturamos el stacktrace completo para logs
    tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"API Exception: {exc.message}\nStacktrace:\n{tb_str}")

    return JSONResponse(status_code=400, content={"detail": exc.message})


async def general_exception_handler(request: Request, exc: Exception):
    # Capturamos cualquier excepción no controlada
    tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"Unexpected error: {str(exc)}\nStacktrace:\n{tb_str}")

    return JSONResponse(
        status_code=500, content={"detail": "Error interno del servidor"}
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
