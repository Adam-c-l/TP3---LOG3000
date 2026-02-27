# Module Templates

## Raison d’être
Ce module contient les templates HTML utilisés par l'application Flask pour rendre les pages web de la calculatrice.

## Fichiers principaux
- `index.html` : Template principal pour la page d'accueil de la calculatrice, incluant le formulaire, les boutons et le JavaScript pour l'interaction.

## Dépendances ou hypothèses
- Utilise Jinja2 pour le rendu des templates (via Flask).
- Assume que les routes Flask fournissent les variables nécessaires, comme `result`.
- Le JavaScript intégré assume un navigateur supportant DOM manipulation basique.
