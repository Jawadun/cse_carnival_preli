# QueueStorm Investigator

Production-ready skeleton for a fintech investigation API.

## Overview

`QueueStorm Investigator` exposes a single endpoint:

- `POST /analyze-ticket`

It receives customer complaints, channel metadata, campaign context, and transaction history, then returns structured investigation insights.

## Tech stack

- Python 3.12
- FastAPI
- LangChain
- langchain-google-genai
- Pydantic v2
- Docker

## Project structure

- `app/api` - FastAPI routing and request/response schemas
- `app/chains` - LangChain orchestration definitions
- `app/prompts` - prompt templates and builders
- `app/models` - domain models and DTOs
- `app/services` - business services and use-case orchestration
- `app/validators` - validation and response contracts
- `app/core` - settings, app startup, dependency injection
- `app/utils` - logging, retry, helper utilities

## Running locally

1. Copy `.env.example` to `.env`
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8080
   ```

## Docker

```bash
docker build -t queue-storm-investigator .
docker run --env-file .env -p 8080:8080 queue-storm-investigator
```
