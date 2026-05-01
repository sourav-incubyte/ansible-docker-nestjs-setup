# Task: Fix Ansible Playbook and NestJS Docker Setup

You are given a broken DevOps setup in `/app`. Your goal is to fix it so the following works:

## What needs to work:
1. The Ansible playbook at `/app/playbook.yml` must run successfully and install Docker on the target host.
2. The docker-compose at `/app/docker-compose.yml` must bring up two services:
   - PostgreSQL on port 5432
   - NestJS app on port 8080
3. The NestJS app must have a working `/checkdb` endpoint that:
   - Connects to PostgreSQL
   - Runs `SELECT 1;`
   - Returns HTTP 200 with `{"status": "ok"}`

## How to run:
```bash
cd /app
ansible-playbook -i inventory.ini playbook.yml
docker-compose up -d
```

## Files are located at:
- `/app/playbook.yml` - Ansible playbook (has bugs)
- `/app/inventory.ini` - Ansible inventory
- `/app/docker-compose.yml` - Docker compose file (has bugs)
- `/app/nestapp/` - NestJS application (has bugs)