ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_NO_DEV=1
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

COPY --from=workspace mcp /app/mcp
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel

RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv /app/nanobot/.venv && \
    uv pip install --python /app/nanobot/.venv/bin/python nanobot-ai && \
    uv pip install --python /app/nanobot/.venv/bin/python -e /app/mcp && \
    uv pip install --python /app/nanobot/.venv/bin/python -e /app/nanobot-websocket-channel

COPY . /app/nanobot


ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

RUN groupadd --system --gid 999 nonroot \
    && useradd --system --gid 999 --uid 999 --create-home nonroot

COPY --from=builder --chown=nonroot:nonroot /app /app

ENV PATH="/app/nanobot/.venv/bin:$PATH"

USER nonroot
WORKDIR /app/nanobot

CMD ["python", "/app/nanobot/entrypoint.py"]
