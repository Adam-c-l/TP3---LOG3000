from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

"""
Ce module implémente une calculatrice web simple utilisant Flask.
Il prend en charge les opérations arithmétiques de base : addition, soustraction, multiplication et division.
"""

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse et retourne le résultat d'une expression arithmétique simple.
    
    Cette fonction prend une expression sous forme de chaîne, l'analyse et calcule le résultat.
    L'expression doit contenir deux opérandes et un opérateur (+, -, *, /).
    Le résultat sera un nombre flottant ou entier selon l'opération.
    
    Paramètres:
    expr (str): L'expression arithmétique, par exemple "2+3"
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")  # Imposer uniquement des opérations binaires simples
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Assurer que l'opérateur n'est pas au début ou à la fin, et qu'il existe
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère les requêtes vers la page d'accueil et traite les calculs.
    
    Cette fonction répond aux requêtes GET et POST pour la route principale.
    Elle récupère l'expression depuis le formulaire POST, la calcule et affiche le résultat.
    Le résultat sera affiché dans le template HTML avec tout message d'erreur.
    
    Paramètres:
    Aucun (fonction route Flask utilisant request global)
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)