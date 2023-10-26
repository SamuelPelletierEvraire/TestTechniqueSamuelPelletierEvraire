import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_root_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello World!'

def test_top_route_valid5(client):
    response = client.get('/top5')
    assert response.status_code == 200
    assert len(response.json) == 5

def test_top_route_valid53(client):
    response = client.get('/top53')
    assert response.status_code == 200
    assert len(response.json) == 53

def test_top_route_invalid(client):
    response = client.get('/top200')
    assert response.status_code == 400