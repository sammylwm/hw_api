FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

ENV UV_TOOL_BIN_DIR=/usr/local/bin

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

ENV PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-playwright

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install playwright

RUN --mount=type=cache,target=/root/.cache/ms-playwright \
    playwright install chromium --with-deps


RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]
