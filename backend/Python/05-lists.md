# Python - Les listes

## Table des matières
- [1. La structure de données (Data Structure)](#1-la-structure-de-données-data-structure)
- [2. La liste](#2-la-liste)
- [3. Les index et les fonctions](#3-les-index-et-les-fonctions)
- [4. Des listes imbriquées dans des listes](#4-des-listes-imbriquées-dans-des-listes)

## 1-La structure de données (Data Structure)
Il s'agit simplement d'une façon de stocker et d'organiser des données. La variable par exemple est une façon de stocker une seule donnée.

## 2-La liste
Une liste est donc une structure de données qui, contrairement à une variable, permet de stocker plusieurs données. Techniquement, une liste peut contenir des données de types complètement différents et sans aucun rapport entre elles mais par convention et pour garder un code clair, il est préférable qu'elles **partagent un lien logique** (comme les villes d'un pays). La liste permet également de conserver l'ordre des données qu'elle contient.

- Les listes sont toujours contenu dans des balises `[]` et chaque item de la liste doit être séparé par une `,` : 

```py
liste = [item1, item2] # Exemple
```
- Les items contenus dans la liste ne sont pas obligés d'être du même type, une liste peut contenir des variables, des chaînes de caractères, des nombres entiers etc: 

```py
marque = "BMW"
info_voitures = [marque, "E46", 2004, False]
# Cependant pour ne pas se mélanger mieux vaut que les données partagent un lien. Ici par exemple j'ai une liste qui contient des infos d'un modèle de voiture que j'apprécie.
```

## 3-Les index et les fonctions
En utilisant une liste, il est possible d'afficher ou manipuler les items qu'elle contient :

- Pour afficher un élément spécifique d'une liste en connaissant son index :

```py
fruits = ["Banane", "Pomme", "Orange", "Fraise"] 
print(fruits[0]) # Affiche le premier item de la liste : "Banane"
print(fruits[3]) # Affiche le dernier item de la liste : "Fraise" 
```
> En informatique, on commence à compter à partir de 0 et non 1. Dans la liste ci-dessus il y a  4 items partant de l'indice 0 à 3 (ordre : de gauche à droite)

- Toujours au niveau de l'affichage, il est possible d'afficher le dernier item d'une liste en utilisant un index négatif : 

```py
fruits = ["Banane", "Pomme", "Orange", "Fraise"]
print(fruits[-1]) # Affiche le dernier item de la liste : "Fraise" 
print(fruits[-2]) # Affiche l'avant dernier item de la liste : "Orange"
print(fruits[-3]) # Affiche l'avant avant dernier item de la liste : "Pomme"
print(fruits[-4]) # Affiche le premier item de la liste : "Banane"
```
> Contrairement aux index positifs qui commencent à 0, les index négatifs commencent à -1 (qui désigne toujours le dernier élément). Il n'existe pas de "-0". La numérotation négative se lit donc indépendamment de la positive, de droite à gauche.

- Il est possible d'obtenir à l'inverse l'index d'un item en utilisant la fonction `.index(item)` :

 ```py
fruits = ["Banane", "Pomme", "Orange", "Fraise"]
print(fruits.index("Banane")) # Affiche la valeur de l'index de l'item correspondant à "Banane", soit 0
```

- Il est possible également dans une liste modifier la valeur d'un item en précisant l'index et en procédant à une réassignation :

```py
fruits = ["Banane", "Pomme", "Orange", "Fraise"]
fruits[0] = "Poire" # On précise qu'on veut manipuler le premier item de la liste, puis on change sa valeur pour poire.
print(fruits) # Affiche la nouvelle liste modifiée : fruits = ["Poire", "Pomme", "Orange", "Fraise"]
```

- Il est possible d'ajouter un ou plusieurs items en utilisant `.append()` et `.extend()`

Avec `.append()` :
```py
fruits.append("Poire") # Ajoute en dernière position dans la liste "Poire" 
```
Avec `.extend()` :

```py
fruits.extend(["Poire", "Bleuet", "Cerise"]) # Ajoute en dernière position dans la liste "Poire", "Bleuet" et "Cerise"
```
> À noter : `.append()` ajoute l'argument qu'on lui passe comme **un seul élément**, même si c'est une liste, elle sera imbriquée (ce concept est expliqué en détail dans la section 4). `.extend()` **déballe** chaque élément d'une liste donnée et les ajoute individuellement.

```py
fruits = ["Banane"]
fruits.append(["Poire", "Cerise"])
print(fruits) # ["Banane", ["Poire", "Cerise"]] : comme UNE seule liste imbriquée

fruits2 = ["Banane"]
fruits2.extend(["Poire", "Cerise"])
print(fruits2) # ["Banane", "Poire", "Cerise"] : chaque élément ajouté séparément
```

> Il est possible de faire bien plus avec une liste, d'où l'importance de consulter et explorer la documentation : https://docs.python.org/3/library/stdtypes.html#typesseq-list

## 4-Des listes imbriquées dans des listes
Il est possible d'imbriquer dans une liste une ou plusieurs listes :

```py
fruits = ["Pomme","Banane","Orange"]
légumes = ["Épinard","Carotte","Laitue"]

fruits_et_légumes = [fruits, légumes]
print(fruits_et_légumes) # Affichera : [["Pomme","Banane","Orange"],["Épinard","Carotte","Laitue"]]
```

- Dans ce cas on veut afficher un item d'une liste, il faut d'abord sélectionner la liste :

```py
fruits = ["Pomme","Banane","Orange"]
légumes = ["Épinard","Carotte","Laitue"]

fruits_et_légumes = [fruits, légumes]
print(fruits_et_légumes[0]) # Afficherait la première liste unique : ["Pomme","Banane","Orange"] 
print(fruits_et_légumes[0][0]) # Afficherait le premier item de la première liste : "Pomme"
```