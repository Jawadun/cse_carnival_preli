from fastapi import FastAPI

from app.api.router import api_router
from app.core.events import register_startup_events
from app.core.settings import settings
from app.utils.logging import configure_logging

app = FastAPI(
    title="QueueStorm Investigator",
    version="0.1.0",
    description="Fintech ticket investigation API",
)

configure_logging(settings)
register_startup_events(app)
app.include_router(api_router)
