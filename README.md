# Boilerplate

FastAPI + React + Hono interview scaffold. Lean by design — structure is ready, logic is not.

## Use this boilerplate

**Clean slate:**
```bash
bunx degit chemalopezp/boilerplate <project-name>
cd <project-name>
git init && git add . && git commit -m "init"
```

**With history:**
```bash
git clone https://github.com/chemalopezp/boilerplate <project-name>
cd <project-name>
git remote remove origin
```

**Push to a new remote when ready:**
```bash
gh repo create <project-name> --private --source=. --push
```

---

## Stack

| Layer | Choice |
|---|---|
| Python backend | FastAPI, SQLModel, asyncpg |
| Node backend | Hono, Prisma, Zod |
| Frontend | React 19, Vite, TypeScript |
| Database | PostgreSQL 16 (Docker) |
| Package managers | `uv` (Python), `bun` (Node) |
| Task runner | `just` |

## Structure

```
api/                        Python backend (:8000)
├── main.py                 create_app() factory + routes
├── config.py               pydantic-settings (reads ASYNC_DATABASE_URL)
├── db.py                   engine, session, SQLModel base
├── schemas.py              Pydantic request/response models
└── services.py             business logic

bff/                        Node/TypeScript backend (:3000)
├── src/index.ts            Hono app + routes
├── src/db.ts               Prisma client singleton
├── src/schemas.ts          Zod schemas
├── src/services.ts         business logic
└── prisma/schema.prisma    DB schema (switch provider for MongoDB)

web/                        React frontend (:5173)
└── src/
    ├── App.tsx
    ├── api/client.ts       typed fetch wrappers
    └── index.css
```

## Running

```bash
just setup                  # first time: installs deps, copies .env, starts postgres

just api-dev                # FastAPI  → http://localhost:8000
just bff-dev                # Hono BFF → http://localhost:3000
just web-dev                # Vite     → http://localhost:5173

just test                   # Python tests
just bff-test               # Node tests
just lint                   # ruff + pyright (Python), eslint (BFF)
```

## JIT Additions

Add only when requirements call for it.

**Migrations (Python):**
```bash
uv add alembic && alembic init alembic
```

**Agent orchestration:**
```bash
uv add langgraph pydantic-ai
```

**LLM:**
```bash
uv add anthropic
```

**Vector search:**
```bash
# change docker-compose image → pgvector/pgvector:pg16
uv add pgvector
```

**MongoDB (BFF):**
```prisma
# bff/prisma/schema.prisma — change provider to "mongodb"
# model IDs must use: @id @default(auto()) @map("_id") @db.ObjectId
```

**Idempotency:** store `Idempotency-Key` + response in Redis; return cached response on replay.

**Sandboxed execution:** `uv add e2b`

**Observability:** `uv add opentelemetry-sdk opentelemetry-instrumentation-fastapi`
