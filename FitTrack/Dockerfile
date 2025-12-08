FROM python:3.10-slim

WORKDIR /app

# system deps for psycopg2, etc. (none needed for this minimal app)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV PORT=8080

EXPOSE 8080

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8080", "--workers", "2"]
