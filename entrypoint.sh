#!/usr/bin/env bash

set -e

echo "Apply alembic migrations"
uv run alembic upgrade head
echo "Successfully applied migrations."

exec "$@"