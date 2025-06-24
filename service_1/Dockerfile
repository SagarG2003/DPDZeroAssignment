# service_1/Dockerfile
FROM golang:1.21-alpine

WORKDIR /app

COPY . .

RUN go mod init service_1 || true  
RUN go build -v -o service1 main.go

EXPOSE 8001

CMD ["go", "run", "main.go"]
