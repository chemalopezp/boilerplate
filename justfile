# Start postgres (port 5432)
db-up:
    docker compose up -d db

# Start FastAPI dev server
api-dev:
    uv run uvicorn api.main:app --reload --port 8000

# Start React dev server
web-dev:
    cd web && bun dev

# Run tests
test:
    uv run pytest -v

# Lint
lint:
    uv run ruff check .

# Format
format:
    uv run ruff format .

# Start Hono BFF dev server
bff-dev:
    cd bff && bun dev

# Test BFF
bff-test:
    cd bff && bun test

# Drop and recreate the database (wipes all data)
db-reset:
    docker compose down -v
    docker compose up -d db
