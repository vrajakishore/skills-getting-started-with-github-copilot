from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    initial_activities = deepcopy(app_module.activities)

    # Arrange
    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))

    yield

    # Cleanup after each test to keep isolation deterministic.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))
