"""
formatter.py

Utility functions for formatting request data before sending it
to the LLM.

These functions DO NOT perform reasoning.

They only convert structured objects into clean text that helps
the LLM understand the data.
"""

from typing import List

from queue_storm.models.request import TransactionHistory


# ==========================================================
# Transaction Formatter
# ==========================================================

def format_transactions(transactions: List[TransactionHistory]) -> str:
    """
    Convert transaction list into readable text.

    This improves prompt quality compared to dumping raw JSON.
    """

    if not transactions:
        return "No transaction history provided."

    lines = []

    for i, tx in enumerate(transactions, start=1):

        lines.append(
            f"""
Transaction {i}
---------------
Transaction ID : {tx.transaction_id}
Timestamp      : {tx.timestamp}
Type           : {tx.type}
Amount         : {tx.amount}
Counterparty   : {tx.counterparty}
Status         : {tx.status}
""".strip()
        )

    return "\n\n".join(lines)


# ==========================================================
# Complaint Formatter
# ==========================================================

def format_complaint(complaint: str) -> str:
    """
    Clean complaint text.
    """

    return complaint.strip()


# ==========================================================
# Optional Metadata Formatter
# ==========================================================

def format_metadata(metadata: dict) -> str:

    if not metadata:
        return "None"

    return "\n".join(
        f"{key}: {value}"
        for key, value in metadata.items()
    )


# ==========================================================
# Build Prompt Payload
# ==========================================================

def build_prompt_payload(request):
    return {
        "ticket_id": request.ticket_id,
        "complaint": format_complaint(request.complaint),
        "transaction_history": format_transactions(request.transaction_history),
        "metadata": format_metadata(request.metadata),
        "language": request.language,
        "channel": request.channel or "unknown",
        "user_type": request.user_type,
        "campaign_context": request.campaign_context or "None",
    }


# ==========================================================
# Optional Pretty Printer
# ==========================================================

def pretty_print_response(response):

    return response.model_dump_json(
        indent=4
    )