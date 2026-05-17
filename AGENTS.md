# Agent Instructions

> For repo structure, stack, and commands see README.md.

## Workflow

1. **Divide first.** Before writing any code, break the request into the smallest logical tasks. Present the list and wait for approval.
2. **One task at a time.** Implement one task, then stop and show the result. Do not proceed to the next task without approval.
3. **Quality gate.** Before marking a task done, run lint and tests. Both must pass.
4. **Never commit.** Stage nothing. The user reviews every file and commits manually.

## Quality gate commands

```bash
# Python
just test && just lint

# Node BFF
just bff-test && cd bff && bun run lint
```

## Code rules

- Prefer less code over covering every edge case.
- Make the basic case work. Flag Day 2 opportunities as a comment — do not implement speculatively.
- No `Request`/`Response` objects in service layer.
- Financial mutations: always use `.with_for_update()`. See `api/db.py`.

## Architecture constraints

**Python backend (`api/`)**
- Entry point: `create_app()` in `api/main.py`. Never a module-level app.
- New routes: inline in `create_app()`, or a separate file added via `app.include_router(...)`.
- Models: extend `SQLModel` with `table=True` in `api/db.py`.
- Schemas: `api/schemas.py`. Services: `api/services.py`.

**Node BFF (`bff/`)**
- New routes: add to `bff/src/index.ts` via `app.get/post(...)`.
- Schemas: Zod in `bff/src/schemas.ts`. Services: `bff/src/services.ts`.
- DB models: add to `bff/prisma/schema.prisma`, then `bunx prisma generate`.

**Frontend (`web/`)**
- All API calls via `web/src/api/client.ts` — no raw `fetch` elsewhere.
- Vite proxies `/api` to `:8000` — no CORS config needed in dev.

## JIT additions

Add only when requirements explicitly call for it. See README "JIT Additions".
