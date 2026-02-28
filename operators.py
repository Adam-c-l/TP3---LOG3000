"""
Ce module définit les opérations arithmétiques de base pour la calculatrice.
"""

def add(a, b):
    """
    Ajoute deux nombres.
    
    Args:
        a (float): Premier opérande.
        b (float): Deuxième opérande.
    
    Returns:
        float: La somme de a et b.
    """
    return a + b


def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier.
    
    Args:
        a (float): Premier nombre.
        b (float): Nombre à soustraire.
    
    Returns:
        float: La différence a - b.
    """
    return a - b


def multiply(a, b):
    """
    Élève le premier nombre à la puissance du deuxième.
    
    Args:
        a (float): Base.
        b (float): Exposant.
    
    Returns:
        float: a élevé à la puissance de b.
    """
    return a * b


def divide(a, b):
    """
    Effectue la division entière du premier nombre par le deuxième.
    
    Args:
        a (float): Nombre à diviser.
        b (float): Diviseur.
    
    Returns:
        int: Le quotient de a divisé par b (division entière).
    """
    return round(a / b, 1)
