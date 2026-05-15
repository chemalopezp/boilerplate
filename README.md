# Boilerplate

FastAPI + React interview scaffold. Lean by design — structure is ready, logic is not.

## Stack

| Layer | Choice |
|---|---|
| Backend | Python 3.12, FastAPI, async SQLAlchemy |
| Frontend | React 19, Vite, TypeScript |
| Database | PostgreSQL 16 (Docker) |
| Package managers | `uv` (Python), `bun` (Node) |
| Task runner | `just` |

## Running

```bash
# 1. Start postgres
just db-up

# 2. Copy env
cp .env.example .env

# 3. Start API
just api-dev        # → http://localhost:8000

# 4. Start frontend (optional)
just web-dev        # → http://localhost:5173

# 5. Tests
just test
```

## Structure

```
api/
├── main.py      create_app() factory + routes
├── config.py    pydantic-settings (reads .env)
├── db.py        engine, session, Base, models
├── schemas.py   Pydantic request/response models
└── services.py  business logic (no HTTP coupling)

web/src/
├── App.tsx
├── api/client.ts  typed fetch wrappers
└── index.css
```

## JIT Additions

Add only when requirements call for it.

**Migrations:**
```bash
uv add alembic && alembic init alembic
# wire alembic/env.py to settings.database_url
```

**Agent orchestration:**
```bash
uv add langgraph pydantic-ai
# add api/agents.py with StateGraph
```

**LLM:**
```bash
uv add anthropic
```

**Vector search:**
```bash
# switch docker-compose image: pgvector/pgvector:pg16
uv add pgvector
```

**Idempotency** (financial side-effect routes):
Store `Idempotency-Key` + response in Redis. Return cached response on replay.

**Sandboxed execution:**
```bash
uv add e2b
```

**Observability:**
```bash
uv add opentelemetry-sdk opentelemetry-instrumentation-fastapi
```
