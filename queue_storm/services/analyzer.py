from queue_storm.chains.investigator_chain import investigator_chain
from queue_storm.guardrails.safety import validate_response
from queue_storm.guardrails.safety import validate_response
from queue_storm.models.request import TicketRequest
from queue_storm.models.response import TicketResponse


class TicketAnalyzer:

    async def analyze(self, request: TicketRequest) -> TicketResponse:

        result = await investigator_chain.invoke(

            {
                "complaint": request.complaint,
                "transaction_history": request.transaction_history,
                "language": request.language,
                "user_type": request.user_type,
                "channel": request.channel,
                "campaign_context": request.campaign_context,
            }

        )
        validate_response(result)
        return result