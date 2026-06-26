from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from queue_storm.api.routes import router
from queue_storm.guardrails.safety import GuardrailViolation
from queue_storm.models.request import TicketRequest
from queue_storm.models.response import TicketResponse
from queue_storm.services import analyzer

app = FastAPI(title="QueueStorm Investigator")
app.include_router(router)


def _api_error_status(exc: Exception) -> int:
    text = str(exc).lower()
    if "resource_exhausted" in text or "quota exceeded" in text or "429" in text:
        return 429
    if "bad request" in text or "invalid" in text:
        return 400
    return 503


@app.exception_handler(GuardrailViolation)
async def guardrail_exception_handler(request: Request, exc: GuardrailViolation):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )


@app.exception_handler(ChatGoogleGenerativeAIError)
async def gemini_exception_handler(request: Request, exc: ChatGoogleGenerativeAIError):
    return JSONResponse(
        status_code=_api_error_status(exc),
        content={"detail": str(exc)},
    )


@app.post("/analyze-ticket", response_model=TicketResponse)
async def analyze(ticket: TicketRequest):
    response = await analyzer.analyze(ticket)
    return response