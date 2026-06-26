from typing import Any


class Formatter:
    @staticmethod
    def format_currency(amount: float) -> str:
        return f"{amount:,.2f}"

    @staticmethod
    def safe_str(value: Any) -> str:
        return str(value) if value is not None else ""
