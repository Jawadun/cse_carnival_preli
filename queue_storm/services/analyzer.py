from queue_storm.chains.investigator_chain import get_investigator_chain
from queue_storm.guardrails.safety import validate_response
from queue_storm.models.request import TicketRequest
from queue_storm.models.response import TicketResponse
from queue_storm.utils.formatter import build_prompt_payload


class TicketAnalyzer:

    async def analyze(self, request: TicketRequest) -> TicketResponse:
        payload = build_prompt_payload(request)
        chain = get_investigator_chain()
        result = await chain.ainvoke(payload)
        validate_response(result)
        return result
