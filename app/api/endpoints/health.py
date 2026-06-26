from fastapi import APIRouter

router = APIRouter()


@router.get("/ready")
async def readiness_probe() -> dict:
    return {"status": "ready"}


@router.get("/live")
async def liveness_probe() -> dict:
    return {"status": "alive"}
