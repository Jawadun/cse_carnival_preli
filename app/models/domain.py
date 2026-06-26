from typing import List
from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_id: str
    timestamp: str
    amount: float
    description: str


class TicketAnalysisRequest(BaseModel):
    customer_complaint: str
    language: str
    channel: str
    user_type: str
    campaign_context: str
    transaction_history: List[Transaction]


class TicketAnalysisResponse(BaseModel):
    relevant_transaction: Transaction
    evidence_verdict: str
    case_type: str
    severity: str
    department: str
    agent_summary: str
    recommended_next_action: str
    customer_reply: str
    human_review_flag: bool
    confidence: float
    reason_codes: List[str]
