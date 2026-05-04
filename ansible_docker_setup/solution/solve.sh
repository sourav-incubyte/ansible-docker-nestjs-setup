#!/bin/bash

set -e

echo "Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs

echo "Copying NestJS application..."
cp -r /solution/nestapp /app/nestapp

echo "Installing NestJS dependencies..."
cd /app/nestapp && npm install

echo "Building NestJS application..."
cd /app/nestapp && npm run build

echo "Creating docker-compose.yml..."
cat > /app/docker-compose.yml <<'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: appdb
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d appdb"]
      interval: 5s
      timeout: 5s
      retries: 5

  nestapp:
    build:
      context: ./nestapp
    ports:
      - "8080:3000"
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_USER: admin
      DB_PASSWORD: secret
      DB_NAME: appdb
    depends_on:
      - postgres
EOF

echo "Installing Docker..."
apt-get update
apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

echo "Installing Docker Compose..."
curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "Starting docker-compose services..."
cd /app && docker-compose up -d --build

echo "Waiting for services to start..."
sleep 30

echo "Done!"
