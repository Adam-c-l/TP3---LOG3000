TP3 log3000

équipe 52
Adam-champagne-Lorrain 2183354


## Description
Ce projet implémente une calculatrice web simple utilisant Flask. L'application permet d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface web monopage.

Portée : Application pour calculs simples sans stockage de données persistantes.

## Installation
### Prérequis
- Python 3.6 ou supérieur
- Pip pour la gestion des paquets

### Guide d'installation étape par étape
1. Cloner le dépôt Git :
   ```
   git clone <URL du dépôt>
   cd TP3---LOG3000
   ```

2. Installer les dépendances :
   ```
   pip install flask
   ```

3. Lancer l'application :
   ```
   python app.py
   ```

## Utilisation
1. Ouvrir un navigateur web et naviguer vers http://localhost:5000

2. Entrer une expression arithmétique dans le champ de texte, par exemple "5 + 3"

3. Cliquer sur le bouton "=" pour calculer le résultat.

Fonctionnalités :
- Opérateurs supportés : +, -, *, /
- Affichage du résultat ou d'erreurs pour expressions invalides.

## Tests
Les tests unitaires seront ajoutés pour valider les fonctions de calcul et les routes.

Pour exécuter les tests (une fois ajoutés) :
```
python -m unittest discover
```
ou
```
pytest
```

## Flux de contribution
- Utiliser Git pour le contrôle de version.
- Créer une branche pour chaque fonctionnalité : `git checkout -b feature/nom-fonctionnalite`
- Commiter avec messages descriptifs.
- Ouvrir une Pull Request pour révision.
- Signaler bugs via Issues GitHub.

Respecter les standards de code et ajouter des tests pour les nouvelles fonctionnalités.
