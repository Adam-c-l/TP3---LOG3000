from app import app
from bs4 import BeautifulSoup

def test_index_get():
    """
    Teste la réponse GET à la page d'accueil.
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'flask calculator' in response.data.lower()

def test_index_post():
    """
    Teste la réponse POST à la page d'accueil avec une expression.
    """
    with app.test_client() as client:
        response = client.post('/', data={'display': '2+3'})
        assert response.status_code == 200
        assert b'5' in response.data

def test_index_post_addition():
    """
    Teste l'affichage du résultat d'une addition via POST.
    """
    with app.test_client() as client:
        response = client.post('/', data={'display': '2+3'})
        assert response.status_code == 200
        assert b'5' in response.data

def test_index_post_multiplication():
    """
    Teste l'affichage du résultat d'une multiplication (puissance) via POST.
    """
    with app.test_client() as client:
        response = client.post('/', data={'display': '2*3'})
        assert response.status_code == 200
        assert b'6' in response.data

def test_button_names():
    """
    Teste que le texte des boutons correspond à leur valeur onclick.
    """
    with app.test_client() as client:
        response = client.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')
        buttons_div = soup.find('div', class_='buttons')
        buttons = buttons_div.find_all('button')
        errors = []
        for button in buttons:
            onclick = button.get('onclick')
            if onclick and onclick.startswith("appendToDisplay('") and onclick.endswith("')"):
                value = onclick[17:-2]
                text = button.get_text()
                if text != value:
                    errors.append(f"Button text '{text}' does not match onclick value '{value}'")
        assert not errors, "\n".join(errors)