FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update  \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY backend/ /app/backend/
COPY .env /app/.env
COPY alembic.ini /app/alembic.ini

ENV PYTHONPATH=/app/

RUN chmod +x /app/backend/entrypoint.sh

ENTRYPOINT ["/app/backend/entrypoint.sh"]
