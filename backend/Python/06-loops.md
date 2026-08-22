# Python - Les boucles

## Table des matières
- [1. Les boucles](#1-les-boucles)
- [2. La boucle `for`](#2-la-boucle-for)
  - [2.1. La boucle `for item in list_item`](#21-la-boucle-for-item-in-list_item)
  - [2.2. La boucle `for item in range(item)`](#22-la-boucle-for-item-in-rangeitem)
  - [2.3. `for item in list_item` vs `for item in range()`](#23-for-item-in-list_item-vs-for-item-in-range)
- [3. La boucle `while`](#3-la-boucle-while)
- [4. Quand utiliser une boucle `while` et une boucle `for`?](#4-quand-utiliser-une-boucle-while-et-une-boucle-for)
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

### 2.3-`for item in list_item` vs `for item in range()`
La vraie différence entre les deux, c'est la source des données parcourues : `for item in list_item` parcourt les éléments déjà existants d'une structure de données, tandis que `for item in range()` génère lui-même une séquence de nombres à parcourir, sans avoir besoin d'une liste préexistante.

```py
for item in list_item:
    # Faire un ou des actions sur chaque élément de la liste

for item in range(1, 11):
    # Faire un ou des actions sur chaque nombre généré
```

## 3-La boucle `while`
La boucle `while` fonctionne comme la boucle for. Elle se distingue cependant sur le mécanisme car dans le cas de ce type de boucle, l'ordinateur va exécuter un bloc de code aussi longtemps que la condition associée reste vraie :

```py
while une_condition_est_vraie:
    # Faire un ou des actions
```

Par exemple :

```py
nombre_de_pas_restant = 5

while nombre_de_pas_restant > 0:
    nombre_de_pas_restant -= 1
    print(f"Il me reste {nombre_de_pas_restant} à faire.")
print("J'ai fait mes pas de la journée")
# Le code va être exécuté tant que le nombre de pas n'a pas atteint 0, donc 5 fois.
# En plus d'afficher à chaque itération le nombre de pas restant
```

## 4-Quand utiliser une boucle `while` et une boucle `for`?
Il est préférable d'utiliser une boucle `while` quand on ne connait pas ou qu'on ne se soucie pas du nombre d'itérations et de l'état d'un sous objet contenu dans une structure de données. On préconise une boucle `for` dans le cas contraire ou lorsqu'on veut une itération définie ou lorsqu'on souhaite savoir quel item d'une structure de données on manipule. 

- Par exemple : valider une saisie utilisateur jusqu'à ce qu'elle soit correcte est un cas classique pour `while`, puisqu'on ne sait pas à l'avance combien de tentatives seront nécessaires.

Il est également bénéfique de savoir que :

- La boucle `while` est plus "dangereuse" que la boucle `for` car contrairement à cette dernière, on n'indique pas de limite aux nombres d'itérations. Si on ne gère pas bien l'état ou le changement de la condition de `True` à `False`, la boucle va persister indéfiniment.