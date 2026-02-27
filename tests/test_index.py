import pytest
from app import app

def test_index_get():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'flask calculator' in response.data.lower()

def test_index_post():
    with app.test_client() as client:
        response = client.post('/', data={'display': '2+3'})
        assert response.status_code == 200
        assert b'5' in response.data

def test_index_post_error():
    with app.test_client() as client:
        response = client.post('/', data={'display': 'abc'})
        assert response.status_code == 200
        assert b'Error' in response.data
