from app.api.schemas.ticket import TicketRequest


class RequestValidator:
    def validate(self, request: TicketRequest) -> TicketRequest:
        # TODO: validate incoming request semantics and required fields
        return request
