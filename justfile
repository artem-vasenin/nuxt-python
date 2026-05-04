@a_default:
    just --list

@dev:
    uv run uvicorn app.main:app --reload --log-config log_conf.yaml

@lint:
    uv run ruff check

@format:
    uv run ruff format

@makemigrations name:
    uv run alembic revision --autogenerate -m "{{name}}"

@migrate:
    uv run alembic upgrade head

@migrate_down steps:
    uv run alembic downgrade -{{steps}}
