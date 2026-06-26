from typing import Literal
from pydantic import BaseModel, Field


class TransactionHistory(BaseModel):
    transaction_id: str = Field(...)
    timestamp: str = Field(...)
    type: Literal[
        "transfer",
        "payment",
        "cash_in",
        "cash_out",
        "settlement",
        "refund",
    ] = Field(...)
    amount: float = Field(...)
    counterparty: str = Field(...)
    status: Literal[
        "completed",
        "failed",
        "pending",
        "reversed",
    ] = Field(...)


class TicketRequest(BaseModel):
    ticket_id: str = Field(...)
    complaint: str = Field(...)
    language: Literal["en", "bn", "mixed"] = Field("en")
    channel: Literal[
        "in_app_chat",
        "call_center",
        "email",
        "merchant_portal",
        "field_agent",
    ] | None = Field(None)
    user_type: Literal["customer", "merchant", "agent", "unknown"] = Field("customer")
    campaign_context: str | None = Field(None)
    transaction_history: list[TransactionHistory] = Field(default_factory=list)
    metadata: dict = Field(default_factory=dict)


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
