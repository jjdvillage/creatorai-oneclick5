FROM python:3.11-slim

# optional: speed & clearer logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy backend code
COPY backend /app

# Render injects $PORT; fall back to 8000 locally
ENV PORT=8000
EXPOSE 8000

# IMPORTANT: bind to $PORT at runtime
CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
