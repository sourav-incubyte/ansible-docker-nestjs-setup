# Bespoke AI Challenge: Ansible Docker Setup Fix

## Mission Briefing

Welcome to the Bespoke AI challenge. You have been provided with a broken DevOps environment.
Your task is to analyze the system and produce a solution in the form of an Ansible playbook that:

1. **Installs Docker** on the target machine.
2. **Deploys a NestJS application** that:
   - Uses **PostgreSQL** as its database.
   - Exposes a health check endpoint.

The setup must work end-to-end when triggered via **Ansible**.

---

## 🔍 Investigation

### The Broken Files

Access the files in the `/app` directory on the target machine.
You will find:
- `playbook.yml` - An Ansible playbook that is currently failing.
- `docker-compose.yml` - A docker-compose file for deploying the services.
- `nestapp/` - A NestJS application configured to use a PostgreSQL database.
- `inventory.ini` - Ansible inventory file.
- `tests/` - Contains tests to validate your solution.

### The Goal

The system should allow you to:

```bash
# Run Ansible to install Docker
ansible-playbook -i inventory.ini playbook.yml

# Deploy the application
docker-compose up -d

# Test the health check
curl http://localhost:8080/checkdb
```

The health check should return:
```json
{"status": "ok"}
```

---

## 🛠️ Your Tasks

### Phase 1: Fix Ansible Playbook

1. **Analyze `playbook.yml`**: Identify why it fails to install Docker.
2. **Fix the playbook**: Ensure it installs Docker successfully.
3. **Verify service name**: Ensure the playbook uses the correct service name for Docker (it should be `docker`, not `dockerd`).

### Phase 2: Fix Docker Compose

1. **Analyze `docker-compose.yml`**: Identify issues with service definitions and environment variables.
2. **Fix the compose file**: Ensure it:
   - Maps PostgreSQL to the correct port (5432).
   - Uses correct environment variable names for the NestJS app.
   - Uses the correct service name for the PostgreSQL container (`postgres`).

### Phase 3: Fix NestJS App

1. **Analyze `nestapp/`**:
   - Check `src/app.controller.ts` for any issues.
   - Ensure the controller uses the correct environment variable names for the database connection.
   - Ensure the health check endpoint is correctly implemented.

### Phase 4: Verification

1. **Fix `tests/test_outputs.py`** if needed.
2. **Run the tests** to validate your solution:
   ```bash
   # From inside the container
   cd /tests
   bash test.sh
   ```

---

## 🎯 Success Criteria

Your solution is successful if:

- ✅ Ansible playbook runs without errors.
- ✅ Docker service starts successfully.
- ✅ Docker Compose brings up both PostgreSQL and NestJS services.
- ✅ NestJS app connects to PostgreSQL successfully.
- ✅ Health check endpoint (`/checkdb`) returns `{"status": "ok"}`.
- ✅ All tests pass.

---

## 📋 Instructions

1. **Analyze** the provided files thoroughly.
2. **Formulate a fix** for each component (Ansible, Docker Compose, NestJS).
3. **Implement** the changes in the respective files.
4. **Test** your solution to ensure it works end-to-end.
5. **Document** your changes by updating the `tests/test_outputs.py` file to reflect the correct behavior.

Good luck! 🚀
