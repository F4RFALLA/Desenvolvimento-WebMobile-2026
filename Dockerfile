FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd -m djangoapp && chown -R djangoapp:djangoapp /app

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

COPY --chown=djangoapp:djangoapp . .

USER djangoapp

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]