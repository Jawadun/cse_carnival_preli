from typing import Literal
from pydantic import BaseModel, Field


class TicketResponse(BaseModel):
    ticket_id: str = Field(...)
    relevant_transaction_id: str | None = Field(None)
    evidence_verdict: Literal[
        "consistent",
        "inconsistent",
        "insufficient_data",
    ] = Field(...)
    case_type: Literal[
        "wrong_transfer",
        "payment_failed",
        "refund_request",
        "duplicate_payment",
        "merchant_settlement_delay",
        "agent_cash_in_issue",
        "phishing_or_social_engineering",
        "other",
    ] = Field(...)
    severity: Literal["low", "medium", "high", "critical"] = Field(...)
    department: Literal[
        "customer_support",
        "dispute_resolution",
        "payments_ops",
        "merchant_operations",
        "agent_operations",
        "fraud_risk",
    ] = Field(...)
    agent_summary: str = Field(...)
    recommended_next_action: str = Field(...)
    customer_reply: str = Field(...)
    human_review_required: bool = Field(...)
    confidence: float = Field(...)
    reason_codes: list[str] = Field(default_factory=list)
