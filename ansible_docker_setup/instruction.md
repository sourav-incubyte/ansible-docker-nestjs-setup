# Fix and Deploy the NestJS + PostgreSQL Stack

## Overview

You are given a DevOps setup located in `/app` that has some configuration issues preventing it from working correctly. Your task is to identify and fix the problems, install Docker, and deploy the application stack.

## Requirements

Your solution must meet the following criteria:

1. **Install Docker and Docker Compose** on the system
2. **Create a docker-compose.yml** to orchestrate the services
3. **Fix any configuration issues** you find in the NestJS application
4. **PostgreSQL** must be accessible on port **5432**
5. **NestJS application** must be accessible on port **8080**
6. **GET /checkdb** endpoint must return **HTTP 200** with JSON: `{"status": "ok"}`

## Files

The following files are available in `/app`:

- `nestapp/` - NestJS application directory
  - `src/app.controller.ts` - API controller
  - `src/app.module.ts` - Application module
  - `src/main.ts` - Application entry point
  - `package.json` - Dependencies
  - `Dockerfile` - Container build configuration

## Deployment

You'll need to:

1. Install Docker and Docker Compose
2. Create a docker-compose.yml configuration for PostgreSQL and NestJS
3. Fix any configuration issues in the NestJS source code
4. Build and start the services

## Notes

- The Docker socket is available at `/var/run/docker.sock` inside the container
- If you modify NestJS source files, rebuild the application before running the playbook:
  ```bash
  cd /app/nestapp && npm run build
  ```
- The PostgreSQL database service is named `postgres` in docker-compose.yml
- PostgreSQL listens on port 5432 inside its container
- After deploying, services will be accessible on their published host ports
- Carefully examine all configuration files to understand the setup

Good luck!