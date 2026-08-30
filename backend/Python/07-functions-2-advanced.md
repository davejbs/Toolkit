# Python - Les fonctions avancées

## Table des matières
- [1. Personnaliser le comportement d'une fonction](#1-personnaliser-le-comportement-dune-fonction)
- [2. Fonctions avec une entrée (input)](#2-fonctions-avec-une-entréeinput)
  - [2.1. Fonctions avec plusieurs entrées](#21-fonctions-avec-plusieurs-entrées)
- [3. Paramètre (Parameter) et Argument (Argument)](#3-paramètreparameter-et-argumentargument)
- [4. Fonctions avec une sortie (output)](#4-fonctions-avec-une-sortieoutput)
---

## 1-Personnaliser le comportement d'une fonction
Il est possible de personnaliser le comportement d'une fonction en la faisant manipuler des données d'une façon spécifique pour ainsi obtenir des fonctions nettement plus complexes

## 2-Fonctions avec une entrée(input)
Il est possible de faire en sorte que les fonctions effectuent des actions par rapport à une donnée qu'on lui fournit:

```py
def ma_fonction(variable):
    # Réaliser quelque choses avec `variable`
    # Puis cette ligne avec `variable`
    # Et cette ligne avec `variable`
```
- Si on veut par exemple réaliser une fonction qui affiche des salutations en fonction du nom qui lui est passé

```py
# Créer la fonction qui reçoit un nom et affiche un message
def salutation(nom):
    print(f"Bonjour {nom}")

# Dans un vrai programme on utiliserait la ligne suivante :
nom_utilisateur = str(input("Veuillez saisir votre nom : "))
# Mais pour cet exemple, on fixe une valeur directement :
nom_utilisateur = "Dave"

salutation(nom_utilisateur) # Affiche "Bonjour Dave"
salutation("Utilisateur") # Affiche "Bonjour Utilisateur"

```
> Si on veut améliorer la lecture du code on peut également passer des indices de type (type hints) :

```py
def salutation(nom : str):
    print(f"Bonjour {nom}")
```
### 2.1-Fonctions avec plusieurs entrées
Il est tout à fait possible de fournir à une fonction plusieurs entrées

```py
def salutation(nom, localisation):
    print(f"Bonjour {nom}")
    print(f"Quelle température fait-il à/au/aux {localisation} ?")

salutation("Dave", "Canada") # Affichera "Bonjour Dave" puis "Quelle température fait-il à/au/aux Canada ?"
```
> Note : L'ordre dans lequel on passe les arguments est important au risque d'obtenir un résultat étrange ou même de faire planter le programme :

- Affiche un résultat étrange

```py
def salutation(nom, localisation):
    print(f"Bonjour {nom}")
    print(f"Quelle température fait-il à/au/aux {localisation} ?")

salutation("Canada", "Dave") # Affichera "Bonjour Canada" puis "Quelle température fait-il à/au/aux Dave ?"
```
- Fait planter le programme : 
```py
def salutation(nom, age):
    age = int(age) # On oblige l'argument à être un entier en le convertissant.
    print(f"Bonjour {nom}")
    print(f"Vous avez {age}")

salutation(21, "Dave") # Va faire planter le programme parce qu'on ne peut pas convertir "Dave" en nombre entier
```

### 3-Paramètre(Parameter) et Argument(Argument)
Généralement, quand on parle de fonctions avec des entrées, il est important de savoir distinguer 2 choses : `parameter` et `argument`.

- Le **paramètre** est le nom de variable défini entre les parenthèses lors de la **création** de la fonction (ex : `nom` dans `def salutation(nom):`)
- L'**argument** est la valeur réelle fournie lors de l'**appel** de la fonction (ex : `"Dave"` dans `salutation("Dave")`)

```py
def salutation(nom): # Ce qui se trouve en parenthèse est un parameter
    print(f"Bonjour {nom}") # Ici aussi

nom_utilisateur = "Dave" 

salutation(nom_utilisateur) # nom_utilisateur est un argument, on passe ce que contient la variable nom_utilisateur au parameter.
salutation("Utilisateur") # "Utilisateur" est un argument, c'est la valeur passée au paramètre de la fonction.
``` 

## 4-Fonctions avec une sortie(output)
[À venir...]