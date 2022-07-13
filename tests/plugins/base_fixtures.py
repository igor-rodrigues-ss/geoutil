import pytest

from typing import Generator

from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as tc:
        yield tc
