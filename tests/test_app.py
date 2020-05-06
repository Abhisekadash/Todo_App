import pytest

import main

@pytest.fixture
def app():
    app = main.app
    client = app.test_client()
    print("starting of application")
    return app

def test_main(client):
    result = client.get("/")
    assert result.status_code == 200
