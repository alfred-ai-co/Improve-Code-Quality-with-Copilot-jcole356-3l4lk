import logging
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("app")

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    logger.error(f"HTTPException: {exc.detail}")
    return JSONResponse(
        {"errors": [exc.detail]},
        status_code=exc.status_code,
    )
