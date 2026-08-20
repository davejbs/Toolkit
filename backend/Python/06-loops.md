# Python - Les boucles

## Table des matières
- [1. Les boucles](#1-les-boucles)
- [2. La boucle `for`](#2-la-boucle-for)
  - [2.1. La boucle `for item in list_item`](#21-la-boucle-for-item-in-list_item)
  - [2.2. La boucle `for item in range(item)`](#22-la-boucle-for-item-in-rangeitem)
- [3. La boucle `while`](#3-la-boucle-while)
---

## 1-Les boucles
En Python, il existe 2 types de boucles : `for` et `while`. 

- La boucle `for` peut parcourir différentes sources : une liste existante (`for item in list_item`) ou une séquence de nombres générée par `range()` (`for i in range(10)`), mais dans les deux cas, le mécanisme reste le même : parcourir chaque élément un par un.

## 2-La boucle `for`
### 2.1-La boucle `for item in list_item`
Pour ce faire, l'ordinateur va exécuter le bloc de code une fois pour chaque élément contenu dans la liste. Pour l'utiliser, il faut définir un item (qui peut être nommé n'importe comment) et une structure de données telle une variable ou une liste qui servira à indiquer une quantité définie.

> Même si item peut être nommé n'importe comment, s'assurer qu'il diffère toujours du nom de la liste existante/structure de données existante

- Cas d'utilisation #1 : Avec des listes :
```py
# Dans le cas d'une liste :
marques_voitures = ["Toyota", "Mazda", "BMW", "Honda", "Subaru", "Ferrari"]
for marque in marques_voitures: # Pour chaque item (marque) de la liste (marques_voitures)
    print(marque) # Affiche la marque
```
- Cas d'utilisation #2 : Avec une variable :

```py
# Dans le cas d'une variable : 
variable = "Message"
for char in variable: # Pour chaque item (caractère) dans la variable (la chaîne de caractères)
    print(char) # Affiche les caractères
```


### 2.2-La boucle `for item in range(item)`
Pour ce faire, l'ordinateur va exécuter le bloc de code une fois pour chaque nombre généré par `range()`. Pour l'utiliser, il faut définir un item (qui peut être nommé n'importe comment) et un nombre qui servira à indiquer une quantité définie. La méthode `range()` peut prendre jusqu'à 3 paramètres : `range(start, stop, step)`.

> Même si item peut être nommé n'importe comment, s'assurer qu'il diffère toujours du nom de la liste existante/structure de données existante

- Cas d'utilisation #1, utiliser ce type de boucle en passant un seul paramètre (start) :

```py
# Dans le cas d'un nombre :
for nombre in range(10): # Pour chaque nombre à l'intérieur du nombre 10
    print(nombre) # Affiche chacun de ces nombres 

# Ou :
nbr = 20
for nombre in range(nbr): # Pour chaque nombre à l'intérieur du nombre 20
    print(nombre) # Affiche chacun de ces nombres
```

- Cas d'utilisation #2, utiliser ce type de boucle en passant deux paramètres pour créer un intervalle (start, stop) :

> Il faut savoir que l'intervalle fonctionne en excluant le nombre passé en paramètre comme arrivée. Par exemple pour boucler 100 fois, il faut mettre : `range(1, 101)` et non `range(1, 100)`

```py
for nombre in range(1, 11): # Pour chaque nombre inclus entre 1 et 10 
    print(nombre) # Affiche chacun de ces nombres
```

- Cas d'utilisation #3 : utiliser ce type de boucle en passant en plus les bonds.

```py
for nombre in range(1, 101, 10): # Pour chaque nombre inclus entre 1 et 100, et par bonds de 10
    print(nombre) # Affiche chacun de ces nombres
```
En passant les bonds, il devient également possible d'opter pour une décrémentation plutôt qu'une incrémentation :

```py
for nombre in range(100, 0, -10): # Pour chaque nombre inclus entre 100 et 1, décrémenter par bonds de 10
    print(nombre) # Affiche chacun de ces nombres
```

## 3-La boucle `while`
[À venir...]