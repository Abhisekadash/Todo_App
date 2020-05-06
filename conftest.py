import main
import pytest

@pytest.fixture
def app():
    app = main.app
    return app

@pytest.fixture
def client():
    app = main.app
    client = app.test_client()
    return client