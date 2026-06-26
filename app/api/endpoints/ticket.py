from fastapi import APIRouter, Depends, HTTPException

from app.api.schemas.ticket import TicketRequest, TicketResponse
from app.services.ticket import TicketAnalysisService
from app.core.deps import get_ticket_analysis_service

router = APIRouter()


@router.post("/analyze-ticket", response_model=TicketResponse)
async def analyze_ticket(
    payload: TicketRequest,
    service: TicketAnalysisService = Depends(get_ticket_analysis_service),
) -> TicketResponse:
    try:
        result = await service.analyze_ticket(payload)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
