import pytest
from app import app, calculate

def test_calculate():
    assert calculate("2+3") == 5.0
    assert calculate("5-2") == 3.0
    assert calculate("2*3") == 8.0
    assert calculate("10/3") == 3.0

def test_calculate_errors():
    with pytest.raises(ValueError):
        calculate("")
    with pytest.raises(ValueError):
        calculate("2++3")
    with pytest.raises(ValueError):
        calculate("abc")

def test_index_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Calculator' in response.data
