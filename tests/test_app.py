import pytest
import requests
import json
import main

@pytest.fixture
def app():
    app = main.app
    print("starting of application")
    return app

def test_main(client):
    result = client.get("/")
    url='https://api.covid19india.org/data.json'

    response=requests.get(url)
    response_data = json.loads(response.text)
    assert result.status_code == response.status_code
