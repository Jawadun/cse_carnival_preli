from typing import List

from app.api.schemas.ticket import TicketResponse


class ResponseValidator:
    def validate(self, response: TicketResponse) -> TicketResponse:
        # TODO: validate the final response contract and business invariants
        errors: List[str] = []
        if response.confidence < 0 or response.confidence > 1:
            errors.append("confidence must be between 0.0 and 1.0")

        if not response.reason_codes:
            errors.append("reason_codes must contain at least one item")

        if errors:
            raise ValueError("Response validation failed: " + "; ".join(errors))

        return response
