import pytest
import requests
import subprocess
import time
import socket


def get_docker_host_ip():
    """Get the Docker host IP address."""
    # Try to get the default gateway (Docker host)
    try:
        result = subprocess.run(
            ['ip', 'route', 'show', 'default'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            # Parse: default via 172.17.0.1 dev eth0
            parts = result.stdout.split()
            if len(parts) >= 3 and parts[0] == 'default' and parts[1] == 'via':
                return parts[2]
    except:
        pass
    
    # Fallback to common Docker gateway
    return '172.17.0.1'


def wait_for_service(url, max_wait=60):
    """Wait for a service to become available."""
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException:
            pass
        time.sleep(1)
    raise TimeoutError(f"Service at {url} did not become available within {max_wait} seconds")


def test_postgres_container_running():
    """Test that PostgreSQL container is running on port 5432."""
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{.Names}} {{.Ports}}'],
        capture_output=True,
        text=True
    )
    assert '5432' in result.stdout, "PostgreSQL should be accessible on port 5432"


def test_nestjs_container_running():
    """Test that NestJS container is running on port 8080."""
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{.Names}} {{.Ports}}'],
        capture_output=True,
        text=True
    )
    assert '8080' in result.stdout, "NestJS should be accessible on port 8080"


def test_checkdb_returns_200():
    """Test that /checkdb endpoint returns HTTP 200."""
    host = get_docker_host_ip()
    response = wait_for_service(f'http://{host}:8080/checkdb')
    assert response.status_code == 200, "Endpoint /checkdb should return 200"


def test_checkdb_returns_ok_json():
    """Test that /checkdb endpoint returns correct JSON with status ok."""
    host = get_docker_host_ip()
    response = wait_for_service(f'http://{host}:8080/checkdb')
    json_data = response.json()
    assert json_data.get('status') == 'ok', "Response should contain status: ok"


def test_checkdb_database_connected():
    """Test that /checkdb endpoint successfully connects to the database."""
    host = get_docker_host_ip()
    response = wait_for_service(f'http://{host}:8080/checkdb')
    json_data = response.json()
    assert json_data.get('status') != 'error', "Database connection should not return error status"