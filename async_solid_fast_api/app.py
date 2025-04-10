from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI


from .core.logger import logger
from .services.external import test


@asynccontextmanager
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    """
    lifespan_fn controls the startup and shutdown of the FastAPI Application.
    This function is called when the FastAPI application starts and stops.

    See FastAPI documentation for more information:
      - https://fastapi.tiangolo.com/advanced/events/
    """

    logger.info("-----SYSTEM STARTUP-----")
    logger.info("------------------------")
    test()

    yield

    logger.info("-----SYSTEM SHUTDOWN----- \n")


app = FastAPI(
    title="async-solid-fast-api",
    description="async-solid-fast-api",
    version="0.0.1",
    lifespan=lifespan_fn,
)


@app.get("/")
async def healthcheck():
    return {"status": "ok"}


def main():
    uvicorn.run(
        "async_solid_fast_api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["async-solid-fast-api"],
        reload_delay=2,
        use_colors=False,
        workers=1,
        forwarded_allow_ips="*",
        log_config=None
    )


if __name__ == "__main__":
    main()
