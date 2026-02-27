from app import app, calculate

def test_calculate_positive_left_and_right():
    """
    Teste le calcul avec addition.
    """
    assert calculate("1+2") == 3.0

def test_calculate_positive_left_and_right():
    """
    Teste le calcul avec multiplication.
    """
    assert calculate("1*2") == 2.0

def test_calculate_positive_left_and_right():
    """
    Teste le calcul avec division.
    """
    assert calculate("1/2") == 0.5

def test_calculate_positive_left_and_right():
    """
    Teste le calcul avec soustraction.
    """
    assert calculate("1-2") == -1.0

