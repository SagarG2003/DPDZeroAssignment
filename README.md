# 🔁 Multi-Service (Golang and Python) Application with Nginx Reverse Proxy and Docker

This project follows a microservice architecture where each backend service runs independently in its own Docker container, and **NGINX** serves as a reverse proxy to route requests to the appropriate service.

### 🔧 Components

- **Service_1**: A Golang backend running on port `8001`, handles routes like `/ping` and `/hello`.
- **Service_2**: A Flask API (Python) backend running on port `8002`, also with `/ping` and `/hello` routes.
- **Nginx**: Acts as a reverse proxy to expose both services on a **single external port (8080)**.
  
All services are containerized and orchestrated with Docker Compose.

---

## 🚀 Getting Started

### ✅ Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🛠️ Build & Run

```bash
docker-compose up --build
```


✅ Test the Endpoints
Once running, all services are accessible via a single port (8080):


| Endpoint                               | Description                 |
| -------------------------------------- | --------------------------- |
| `http://localhost:8080/service1/ping`  | Health check for Go service |
| `http://localhost:8080/service1/hello` | Hello from Go service       |
| `http://localhost:8080/service2/ping`  | Health check for Flask API  |
| `http://localhost:8080/service2/hello` | Hello from Flask API        |

---

## 🔀 How Routing Works 
1. All HTTP requests are made to `http://localhost:8080`.
2. NGINX inspects the request URL:
   - Routes starting with `/service1/` are forwarded to `service_1:8001`
   - Routes starting with `/service2/` are forwarded to `service_2:8002`
3. The respective backend responds to the request.
4. NGINX sends the response back to the client.

### 🔗 Internal Routing

| Public Endpoint                  | Internal Proxy Target            |
|----------------------------------|----------------------------------|
| `/service1/ping`                | `http://service_1:8001/ping`     |
| `/service2/hello`               | `http://service_2:8002/hello`    |

> NGINX automatically strips the `/service1` or `/service2` prefix before forwarding.

### Note: All containers run on the same Docker bridge network, enabling hostname-based service discovery (`service_1`, `service_2`).

---

## 📄 Logging and Health Monitoring 

This system uses **NGINX access logs** to capture and record incoming requests with full metadata. Here's how logging and health monitoring work:

### 📥 Incoming Request Logs

Each route hit through the proxy is logged with:

- **Timestamp**
- **Client IP**
- **HTTP Method & Path**
- **Status Code**
- **User-Agent**

#### 🔧 Log Format (defined in `nginx.conf`)

```nginx
log_format main_log '$remote_addr - [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_user_agent"';
```
---

## 🏗️ Bonus

## Multi-stage Docker Builds for Minimun Docker Image Size

To optimize performance and reduce Docker image size, both services are built using multi-stage Docker builds.
- Service_1: Reduced docker image size from 140MB to 15MB
- Service_2: Reduced docker image size from 200MB to 130MB

📦 Why Use Multi-Stage Builds?

 ~ Faster container startup time

 ~ Smaller attack surface

 ~ No unused build tools or dependencies in production

## 🧩 Use of ASGI with flask and Uvicorn (Service_2)

I have used ASGI server because as per requirement the code was running with uvicorn rather with python. So, to ensure performance and compatibility with uvicorn and docker ASGI server is used in python (flask) application.

## 🔍 Logging and Monitoring with Prometheus and Grafana 

**Prometheus** scrapes and stores metrics from our golang and python services (e.g., /metrics endpoint).

**Grafana** reads those metrics from Prometheus and displays them on interactive dashboards.
