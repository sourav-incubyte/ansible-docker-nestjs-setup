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


Good luck!