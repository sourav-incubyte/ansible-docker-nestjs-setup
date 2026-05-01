import pytest
import subprocess
import requests
import time


def test_playbook_service_name_fixed():
    """Test that playbook uses 'docker' not 'dockerd'"""
    with open('/app/playbook.yml', 'r') as f:
        content = f.read()
    assert 'name: dockerd' not in content, "playbook.yml still has 'dockerd' - should be 'docker'"
    assert 'name: docker' in content, "playbook.yml should have service name 'docker'"


def test_docker_compose_postgres_port_fixed():
    """Test that postgres is mapped to port 5432 not 5433"""
    with open('/app/docker-compose.yml', 'r') as f:
        content = f.read()
    assert '5433:5432' not in content, "docker-compose.yml still has wrong port 5433"
    assert '5432:5432' in content, "docker-compose.yml should map postgres to port 5432"


def test_docker_compose_db_host_fixed():
    """Test that DB_HOST is 'postgres' not 'database'"""
    with open('/app/docker-compose.yml', 'r') as f:
        content = f.read()
    assert 'DB_HOST: database' not in content, "docker-compose.yml still has wrong DB_HOST"
    assert 'DB_HOST: postgres' in content, "docker-compose.yml should have DB_HOST: postgres"


def test_nestjs_checkdb_endpoint_fixed():
    """Test that NestJS controller has /checkdb not /healthz"""
    with open('/app/nestapp/src/app.controller.ts', 'r') as f:
        content = f.read()
    assert '/healthz' not in content, "app.controller.ts still has '/healthz' endpoint"
    assert '/checkdb' in content, "app.controller.ts should have '/checkdb' endpoint"


def test_docker_compose_has_correct_structure():
    """Test docker-compose has both required services"""
    with open('/app/docker-compose.yml', 'r') as f:
        content = f.read()
    assert 'postgres' in content, "docker-compose.yml missing postgres service"
    assert 'nestapp' in content, "docker-compose.yml missing nestapp service"
    assert '8080' in content, "docker-compose.yml missing port 8080"


def test_nestjs_uses_env_variables():
    """Test that NestJS controller uses environment variables for DB connection"""
    with open('/app/nestapp/src/app.controller.ts', 'r') as f:
        content = f.read()
    assert 'DB_HOST' in content, "app.controller.ts missing DB_HOST env variable"
    assert 'DB_PORT' in content, "app.controller.ts missing DB_PORT env variable"
    assert 'DB_USER' in content, "app.controller.ts missing DB_USER env variable"