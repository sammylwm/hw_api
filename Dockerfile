FROM python:3.11-slim

WORKDIR /data
COPY pyproject.toml .

RUN pip install uv
RUN uv sync
#
#RUN pip install playwright \
#    && playwright install --with-deps

EXPOSE 8000

# Запуск приложения
CMD ["uv", "run", "main.py"]
