# Deploy a Database-Connected API

## Task

Deploy a web application that connects to a PostgreSQL database and provides a health check endpoint.

## Requirements

1. **PostgreSQL database** running on port **5432**
2. **Web API** running on port **8080**
3. **GET /checkdb** endpoint that:
   - Connects to the database
   - Returns HTTP 200
   - Returns JSON: `{"status": "ok"}`

## Environment

- You have access to `/var/run/docker.sock` for container management
- You are working in the `/app` directory
- You have root access to install any required tools

## Hints

- Use PostgreSQL 15 or compatible
- Database credentials: user=`admin`, password=`secret`, database=`appdb`
- The API should use Node.js/NestJS framework
- Use Docker Compose to orchestrate services

Good luck!