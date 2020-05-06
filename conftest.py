import main
import pytest

@pytest.fixture
def app():
    app = main()
    return app