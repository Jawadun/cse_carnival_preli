# QueueStorm Investigator

QueueStorm Investigator is a fintech investigation API that analyzes customer dispute tickets and transaction history, then returns structured investigation recommendations for support agents.

## Setup instructions

1. Copy `.env.example` to `.env`
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Start the app locally:
   ```bash
   uvicorn queue_storm.app:app --host 0.0.0.0 --port 8080
   ```

## Run command

```bash
uvicorn queue_storm.app:app --host 0.0.0.0 --port 8080
```

## Tech stack

- Python 3.12
- FastAPI for the HTTP API
- LangChain for LLM orchestration
- `langchain-google-genai` for Gemini model integration
- Pydantic v2 for request/response validation
- Docker for containerization

## AI approach

The service uses a deterministic LangChain pipeline:

- `PromptTemplate` / `ChatPromptTemplate` for structured system/human instructions
- `ChatGoogleGenerativeAI` as the Gemini model adapter
- `RunnableSequence` to compose prompt + structured output
- Response parsing into a strict `TicketResponse` Pydantic schema

The model is guided to:

- treat the ticket as an investigation task
- analyze both complaint text and transaction history
- identify whether a specific transaction matches the complaint
- return `insufficient_data` when evidence is ambiguous
- avoid guessing or approving refunds/reversals

## Safety logic

The service includes guardrails for:

- forbidden security phrases
- forbidden refund/reversal promises
- suspicious third-party contact suggestions
- valid enum values for case type, department, evidence, and severity
- confidence range enforcement
- department routing consistency
- human review requirements for critical or phishing-related cases

Guardrails raise structured validation failures and are exposed as HTTP `400` responses.

## Model and cost reasoning

- Uses Gemini model `gemini-2.5-flash` for reliable structured output and reasoning.
- Chooses a low temperature (`0`) for deterministic behavior.
- Uses retry and timeout settings to reduce transient API failures.
- Realistic deployment should monitor Gemini quota and cost usage carefully, especially with free-tier limits.

## MODELS

- `gemini-2.5-flash`
  - Runs on Google Gemini cloud via the `langchain-google-genai` adapter.
  - Chosen for its structured-output capabilities, strong reasoning over transaction data, and support for deterministic prompt guidance.
  - The model is used exclusively in the cloud; no local model is required.

## Sample output

See `QueueStorm_Preli_Sample_Cases.json` for a public sample case, the request payload, and expected JSON output from the service.

## Assumptions

- Input includes complaint, transaction history, channel, language, and optional metadata.
- A relevant transaction is only selected when complaint details clearly match one unique transaction.
- Vague complaints should return `insufficient_data` rather than guessing.
- The model output is validated before it is returned to clients.

## Known limitations

- Current runtime depends on Gemini API availability and quota.
- The LLM may still require prompt tuning for edge-case complaint semantics.
- The service does not currently store ticket history or perform retries beyond the configured model client retries.
- Guardrails are deterministic and may need extension for additional fraud or compliance rules.
