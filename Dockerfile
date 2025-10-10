FROM ghcr.io/astral-sh/uv:python3.14-trixie

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv run playwright install chromium --with-deps

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]
