from fastapi import FastAPI

from app.core.settings import settings


def register_startup_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        # TODO: initialize resources, clients, telemetry, DI container
        pass


    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        # TODO: gracefully close resources and connections
        pass
