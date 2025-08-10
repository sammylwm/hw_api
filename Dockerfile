FROM python:3.13.4-bookworm


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
WORKDIR /data

RUN pip install --upgrade pip "uv==0.6.3"

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev

ENV PATH="/data/.venv/bin:$PATH"

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]
