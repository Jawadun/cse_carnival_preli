from langchain_google_genai import ChatGoogleGenerativeAI

from queue_storm.config import settings
from queue_storm.prompts.investigator_prompt import prompt
from queue_storm.models.response import TicketResponse


_investigator_chain = None


def get_investigator_chain():
    global _investigator_chain
    if _investigator_chain is not None:
        return _investigator_chain

    if not settings.gemini_api_key:
        raise RuntimeError(
            "Gemini API key is required. Set GEMINI_API_KEY in the environment."
        )

    llm = ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        api_key=settings.gemini_api_key,
        temperature=0,
        retries=settings.gemini_retries,
        request_timeout=settings.gemini_timeout,
    )
    structured_llm = llm.with_structured_output(TicketResponse)
    _investigator_chain = prompt | structured_llm
    return _investigator_chain