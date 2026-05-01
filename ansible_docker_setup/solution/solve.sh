#!/bin/bash

# Fix 1: Fix the Ansible playbook - change 'dockerd' to 'docker'
sed -i 's/name: dockerd/name: docker/' /app/playbook.yml

# Fix 2: Fix docker-compose.yml - change port 5433 to 5432
sed -i 's/5433:5432/5432:5432/' /app/docker-compose.yml

# Fix 3: Fix docker-compose.yml - change DB_HOST from 'database' to 'postgres'
sed -i 's/DB_HOST: database/DB_HOST: postgres/' /app/docker-compose.yml

# Fix 4: Fix the NestJS controller - change '/healthz' to '/checkdb'
sed -i "s|@Get('/healthz')|@Get('/checkdb')|" /app/nestapp/src/app.controller.ts

# Start docker service
service docker start || true
sleep 3

# Build and start services
cd /app
docker-compose up -d --build

# Wait for services to be ready
sleep 30

echo "Solution applied successfully"