from fastapi import FastAPI

from queue_storm.api.routes import router
from queue_storm.models.request import TicketRequest
from queue_storm.services import analyzer

app = FastAPI(title="QueueStorm Investigator")
app.include_router(router)


@app.post("/analyze-ticket")
async def analyze(ticket: TicketRequest):
    response = await analyzer.analyze(ticket)
    return response