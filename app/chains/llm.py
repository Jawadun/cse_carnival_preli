from app.api.schemas.ticket import TicketRequest, TicketResponse


class TicketAnalysisChain:
    def __init__(self) -> None:
        # LangChain pipeline stubbed for server startup.
        pass

    async def run(self, request: TicketRequest) -> TicketResponse:
        # TODO: implement LangChain pipeline using ChatGoogleGenerativeAI and StructuredOutput.
        return TicketResponse(
            ticket_id=request.ticket_id,
            relevant_transaction_id=None,
            evidence_verdict="insufficient_data",
            case_type="other",
            severity="low",
            department="customer_support",
            agent_summary="Investigation stub: no analysis implemented yet.",
            recommended_next_action="Escalate to human review for investigation.",
            customer_reply="We have received your case and will review it shortly.",
            human_review_required=True,
            confidence=0.0,
            reason_codes=["pending_analysis"],
        )
