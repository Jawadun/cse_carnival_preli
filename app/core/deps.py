from app.services.ticket import TicketAnalysisService


def get_ticket_analysis_service() -> TicketAnalysisService:
    return TicketAnalysisService()
