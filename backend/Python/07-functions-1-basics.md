# Python - Les fonctions

## Table des matières
- [1. Les fonctions, qu'est-ce que c'est ?](#1-les-fonctions-quest-ce-que-cest-)
- [2. Comment créer une fonction ?](#2-comment-créer-une-fonction-)

---


## 1-Les fonctions, qu'est-ce que c'est ?
Les fonctions sont `des blocs de codes réutilisables` permettant d'accomplir une tâche précise et très souvent redondante. Les fonctions permettent également de rendre le code plus lisible en réduisant ou du moins en cachant les longs blocs de codes dans des fichiers à part qu'on pourra par la suite importer en tant que module. Python possède d'ailleurs des fonctions natives comme le `print()`, `len()` etc. En voici quelques unes : 


| Fonction | Catégorie | Description | Exemple |
|---|---|---|---|
| `print()` | Affichage | Affiche du texte dans la console | `print("Bonjour")` |
| `input()` | Saisie | Récupère une saisie utilisateur | `input("Nom : ")` |
| `len()` | Mesure | Retourne la longueur (nombre d'éléments/caractères) | `len("chat")` → `4` |
| `type()` | Introspection | Retourne le type d'une donnée | `type(21)` → `<class 'int'>` |
| `int()` | Conversion | Convertit en nombre entier | `int("5")` → `5` |
| `float()` | Conversion | Convertit en nombre décimal | `float("5")` → `5.0` |
| `str()` | Conversion | Convertit en chaîne de caractères | `str(5)` → `"5"` |
| `bool()` | Conversion | Convertit en booléen | `bool(1)` → `True` |
| `round()` | Mathématique | Arrondit un nombre | `round(3.7)` → `4` |
| `abs()` | Mathématique | Valeur absolue | `abs(-5)` → `5` |
| `min()` | Mathématique | Retourne la plus petite valeur | `min(3, 1, 2)` → `1` |
| `max()` | Mathématique | Retourne la plus grande valeur | `max(3, 1, 2)` → `3` |
| `sum()` | Mathématique | Additionne les éléments d'une liste | `sum([1, 2, 3])` → `6` |
| `sorted()` | Liste | Retourne une liste triée | `sorted([3, 1, 2])` → `[1, 2, 3]` |
| `range()` | Génération | Génère une séquence de nombres | `range(5)` → `0,1,2,3,4` |


> Note : Pour en apprendre davantage ou comprendre comment les utiliser, se référer à la documentation officielle : https://docs.python.org/3/library/functions.html

## 2-Comment créer une fonction ?
Pour créer une fonction, il faut d'abord mettre le mot `def` puis donner un nom à la fonction, par exemple `ma_fonction`, puis ensuite des parenthèses `()` et puis terminer par un deux-points `:`. Par la suite il suffit d'indenter le bloc de code que la fonction doit exécuter.

```py
def ma_fonction():
    # Réaliser cette ligne
    # Puis cette ligne
    # Et cette ligne
```
