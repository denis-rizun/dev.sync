#!/bin/sh

set -e

cd /app

if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

echo "[ALEMBIC]: Running..."
alembic -c backend/alembic.ini upgrade head

echo "[FASTAPI]: Running..."
exec uvicorn backend.main:app --host 0.0.0.0 --port "${API_PORT}"
