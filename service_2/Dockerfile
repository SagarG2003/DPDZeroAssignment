# service_2/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask uvicorn asgiref

EXPOSE 8002

CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "8002"]
