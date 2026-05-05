@a_default:
    just --list

@dev:
    uv run uvicorn app.main:app --reload --log-config log_conf.yaml

@lint:
    uv run ruff check

@format:
    uv run ruff format

@db:
    uv run psql -h localhost -p 5433 -U postgres -d board

@makemigrations name:
    uv run alembic revision --autogenerate -m "{{name}}"

@migrate:
    uv run alembic upgrade head

@migrate_down steps:
    uv run alembic downgrade -{{steps}}
