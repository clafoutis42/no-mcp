ARG     VARIANT=3.14.2-slim

# Setup building env ###################################################################
FROM "python:${VARIANT}" AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    UV_LINK_MODE=copy \
    UV_SYSTEM_PYTHON=true \
    VIRTUAL_ENV="/app/.venv"

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

ENV MCP_TRANSPORT=http

# Prepare building tools ###############################################################
FROM base AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable --no-dev

# Development image for local ##########################################################
FROM builder AS development

ENV PATH="/root/.local/bin:$PATH"

# This will be removable once Ruff is pulled from original package instead of fork
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    --mount=type=tmpfs,target=/var/log \
    apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends build-essential git

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable && \
    uv tool install poethepoet

EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload", "app.presentation.mcp.app:init_asgi_app"]


# Production/staging image #############################################################
FROM base AS production

# Create a non-root user to run the app and own app-specific files
RUN useradd -r -u 1000 -s /bin/bash -m -d /app no-mcp

COPY --chown=no-mcp --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

COPY --chown=no-mcp ./app ./app/
COPY --chown=no-mcp ./config/gunicorn.py ./config.py

RUN --mount=from=builder,source=/bin/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=README.md,target=README.md \
    uv sync --no-dev --frozen --no-editable --compile-bytecode

USER no-mcp

EXPOSE 8000
CMD ["gunicorn", "-c", "config.py", "app.presentation.mcp.app:init_asgi_app"]
