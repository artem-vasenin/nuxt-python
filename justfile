@a_default:
    just --list

@dev:
    uv run uvicorn app.main:app --reload --log-config log_conf.yaml

@lint:
    uv run ruff check

@format:
    uv run ruff format
