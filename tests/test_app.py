import pytest

import main

def test_main(client):
    result = client.get("/")
    assert result.status_code == 200
