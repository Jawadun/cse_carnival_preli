from langchain_google_genai import ChatGoogleGenerativeAI

from queue_storm.prompts.investigator_prompt import prompt
from queue_storm.models.response import TicketResponse


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    retries=3,
    request_timeout=30,
)

structured_llm = llm.with_structured_output(TicketResponse)

investigator_chain = prompt | structured_llm