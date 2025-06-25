# # Dockerfile for service_2
# This Dockerfile builds a python application and runs it in an python container with multistage builds. Size of docker image is reduced by from 200MB to 130MB

# Stage 1: Builder
FROM python:3.10-slim AS builder

WORKDIR /install

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install flask uvicorn asgiref

# Stage 2: Minimal runtime
FROM python:3.10-slim

WORKDIR /app

# Copy only necessary runtime packages
COPY --from=builder /install /usr/local

COPY app.py .

EXPOSE 8002


CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "8002"]
