import pytest
from app import app as create_app


@pytest.fixture()
def app():
    app = create_app
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/")
    assert b"<p>Hello World!!!</p>" in response.data
