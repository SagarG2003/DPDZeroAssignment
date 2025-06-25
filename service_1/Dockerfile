# Dockerfile for service_1
# This Dockerfile builds a Go application and runs it in an Alpine container with multistage builds. Size of docker image is reduced by from 140Mb to 15Mb.

# Stage 1: Builder
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy source code
COPY . .

RUN go mod init service_1 || true

# Build the binary
RUN go build -v -o service1 main.go

# Stage 2: Runner
FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/service1 .

EXPOSE 8001

CMD ["./service1"]
