from fastapi import APIRouter

from app.api.endpoints.health import router as health_router
from app.api.endpoints.ticket import router as ticket_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(ticket_router, prefix="", tags=["ticket"])
