# Agent Instructions

## Code generation rules
- Generate one logical piece at a time. Stop after each and wait for approval.
- Prefer less code over covering every edge case.
- Make the basic case work. Flag Day 2 scaling opportunities as a comment — do not implement speculatively.
- **Never commit.** The user reviews every file personally before staging or committing. Do not run `git add`, `git commit`, or `git push`.

## Architecture
- Entry point: `api/main.py` → `create_app()` factory. Never use a module-level app.
- New routes: add a new `@app.get/post(...)` inside `create_app()`, or extract to a file and include via `app.include_router(...)`.
- Business logic: `api/services.py`. No `Request`/`Response` objects there.
- Pydantic schemas: `api/schemas.py`.
- Database models: add to `api/db.py` extending `Base`. Session dependency: `get_session`.
- Financial mutations: always use `.with_for_update()`. See comment in `api/db.py`.

## Frontend
- All API calls via `web/src/api/client.ts` — no raw `fetch` elsewhere.
- Vite proxies `/api` to `localhost:8000` — no CORS config needed in dev.

## Running
- `just db-up`  → postgres on :5432
- `just api-dev` → FastAPI on :8000
- `just web-dev` → Vite on :5173
- `just test`   → pytest
- `just lint`   → ruff

## JIT — add only when requirements call for it
See README "JIT Additions" for exact commands.
