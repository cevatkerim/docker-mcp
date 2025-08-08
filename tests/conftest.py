from __future__ import annotations

from unittest.mock import MagicMock
import types
import pytest


@pytest.fixture()
def mock_docker_client():
    client = MagicMock()
    client.api = MagicMock()
    client.version.return_value = {"Version": "25.0.0"}
    client.ping.return_value = True
    # Containers and volumes managers
    client.containers = MagicMock()
    client.volumes = MagicMock()
    return client


@pytest.fixture()
def fake_container():
    c = MagicMock()
    c.id = "abc123"
    c.name = "test-cont"
    c.status = "running"
    c.image = types.SimpleNamespace(tags=["python:3.9-slim"])
    c.attrs = {"State": {"Status": "running"}, "Created": "2025-01-01T00:00:00Z"}
    return c

