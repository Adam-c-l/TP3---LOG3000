from operators import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 4) == 16
    assert multiply(5, 5) == 25
    assert multiply(1, 0) == 1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 3) == 3.3
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0
