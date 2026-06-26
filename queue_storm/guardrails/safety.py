"""
QueueStorm Guardrail Engine

This module performs deterministic validation of the LLM output
before it is returned to the API client.

The LLM is NOT trusted.

If a rule is violated,
raise an exception or regenerate the response.
"""

from typing import Dict

from models.response import TicketResponse


# ==========================================================
# Allowed Enum Values
# ==========================================================

VALID_CASE_TYPES = {
    "wrong_transfer",
    "payment_failed",
    "refund_request",
    "duplicate_payment",
    "merchant_settlement_delay",
    "agent_cash_in_issue",
    "phishing_or_social_engineering",
    "other",
}

VALID_EVIDENCE = {
    "consistent",
    "inconsistent",
    "insufficient_data",
}

VALID_DEPARTMENTS = {
    "customer_support",
    "dispute_resolution",
    "payments_ops",
    "merchant_operations",
    "agent_operations",
    "fraud_risk",
}

VALID_SEVERITY = {
    "low",
    "medium",
    "high",
    "critical",
}


# ==========================================================
# Department Mapping
# ==========================================================

CASE_TO_DEPARTMENT = {
    "wrong_transfer": "dispute_resolution",
    "payment_failed": "payments_ops",
    "duplicate_payment": "payments_ops",
    "merchant_settlement_delay": "merchant_operations",
    "agent_cash_in_issue": "agent_operations",
    "phishing_or_social_engineering": "fraud_risk",
    "other": "customer_support",
}


# refund_request can belong to two departments
REFUND_DEPARTMENTS = {
    "customer_support",
    "dispute_resolution",
}


# ==========================================================
# Forbidden Words
# ==========================================================

FORBIDDEN_SECURITY = [

    "otp",

    "pin",

    "password",

    "full card",

    "card number",

    "cvv",

]

FORBIDDEN_PROMISES = [

    "we will refund",

    "refund has been approved",

    "money has been refunded",

    "we reversed",

    "account unblocked",

    "we recovered",

]

SUSPICIOUS_CONTACT = [

    "telegram",

    "whatsapp",

    "facebook inbox",

    "gmail.com",

    "contact this number",

]


# ==========================================================
# Exceptions
# ==========================================================

class GuardrailViolation(Exception):
    pass


# ==========================================================
# Helper
# ==========================================================

def contains_any(text: str, words: list[str]) -> bool:

    text = text.lower()

    return any(word in text for word in words)


# ==========================================================
# Safety Validation
# ==========================================================

def validate_customer_reply(reply: str):

    if contains_any(reply, FORBIDDEN_SECURITY):

        raise GuardrailViolation(
            "Customer reply requests sensitive credentials."
        )

    if contains_any(reply, FORBIDDEN_PROMISES):

        raise GuardrailViolation(
            "Customer reply promises refund/reversal."
        )

    if contains_any(reply, SUSPICIOUS_CONTACT):

        raise GuardrailViolation(
            "Customer reply directs user to unofficial support."
        )


# ==========================================================
# Enum Validation
# ==========================================================

def validate_enums(result: TicketResponse):

    if result.case_type not in VALID_CASE_TYPES:

        raise GuardrailViolation("Invalid case_type.")

    if result.department not in VALID_DEPARTMENTS:

        raise GuardrailViolation("Invalid department.")

    if result.evidence_verdict not in VALID_EVIDENCE:

        raise GuardrailViolation("Invalid evidence_verdict.")

    if result.severity not in VALID_SEVERITY:

        raise GuardrailViolation("Invalid severity.")


# ==========================================================
# Confidence Validation
# ==========================================================

def validate_confidence(result: TicketResponse):

    if not 0 <= result.confidence <= 1:

        raise GuardrailViolation(
            "Confidence must be between 0 and 1."
        )


# ==========================================================
# Department Validation
# ==========================================================

def validate_department(result: TicketResponse):

    if result.case_type == "refund_request":

        if result.department not in REFUND_DEPARTMENTS:

            raise GuardrailViolation(
                "Invalid department for refund_request."
            )

        return

    expected = CASE_TO_DEPARTMENT.get(result.case_type)

    if expected is None:

        return

    if expected != result.department:

        raise GuardrailViolation(

            f"{result.case_type} must route to {expected}"

        )


# ==========================================================
# Human Review Validation
# ==========================================================

def validate_human_review(result: TicketResponse):

    should_review = (

        result.severity == "critical"

        or result.case_type == "phishing_or_social_engineering"

        or result.evidence_verdict == "insufficient_data"

    )

    if should_review and not result.human_review_required:

        raise GuardrailViolation(

            "Human review should be enabled."

        )


# ==========================================================
# Main Entry
# ==========================================================

def validate_response(result: TicketResponse):

    validate_customer_reply(result.customer_reply)

    validate_enums(result)

    validate_confidence(result)

    validate_department(result)

    validate_human_review(result)

    return result