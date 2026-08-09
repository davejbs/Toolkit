# Python - Les structures de contrôle et opérateurs logiques

## Table des matières
- [1. Les opérateurs de comparaison mathématique](#1-les-opérateurs-de-comparaison-mathématique)
- [2. Les états binaires](#2-les-états-binaires)
- [3. Les conditions](#3-les-conditions)
- [4. Les opérateurs logiques](#4-les-opérateurs-logiques)
- [5. Plusieurs conditions](#5-plusieurs-conditions)
- [6. Tableau résumé](#6-tableau-résumé)
- [7. Les structures de contrôle](#7-les-structures-de-contrôle)
- [8. Les structures de contrôle imbriquées](#8-les-structures-de-contrôle-imbriquées)

---
## 1-Les opérateurs de comparaison mathématique
Avant d'aller plus loin, il est important de présenter les opérateurs de comparaison mathématiques :

| Opérateur | Signification |
|---|---|
| `==` | Égal à |
| `!=` | Différent de |
| `<` | Plus petit que |
| `>` | Plus grand que |
| `<=` | Plus petit ou égal à | 
| `>=` | Plus grand ou égal à | 

## 2-Les états binaires
Il existe en Python (comme en programmation en général) deux états binaires : vrai (`True`, équivalent à `1`) et faux (`False`, équivalent à `0`).
```py
print(True == 1)  # True
print(False == 0) # True
```

## 3-Les conditions
Les opérateurs mathématiques permettent de concevoir des conditions pour que l'ordinateur puisse ensuite vérifier si ces dernières sont vraies (`True`) ou fausses(`False`).

- Une simple condition possède généralement 2 termes : Une donnée, un opérateur de comparaison mathématique et une autre donnée à comparer : 

```py
age = 21
age <= 18 # Un premier terme (age), un opérateur mathématique de comparaison(<=) et un deuxième terme à comparer (18)
# Retourne "False" comme résultat parce que 21 est plus grand que 18
```
- D'autres exemples : 

| Exemple | Résultat |
|---|---|
| `5 == 5` | `True` |
| `5 != 3` | `True` |
| `3 < 5` | `True` |
| `5 > 3` | `True` |
| `5 <= 5` | `True` |
| `5 >= 6` | `False` |


## 4-Les opérateurs logiques
Puisqu'il existe 2 états binaires en Python : vrai (`True`) et faux (`False`), les opérateurs logiques servent donc à manipuler des conditions ou les vérifier. Il en existe 3 : 
- or
- and
- not

## 5-Plusieurs conditions
Il est également plausible de jumeler plus d'une condition ensemble à l'aide d'opérateurs logiques. Selon leur utilisation, il pourront changer la valeur globale d'une condition.

- Avec l'opérateur `or`, il suffit qu'une des 2 conditions soit vraie pour que l'ensemble le soit également. :

```py
# Exemple avec une seule condition
True or False # Donnera True parce qu'un des 2 termes est vrai.
```
- Autre exemple

```py
# Exemple avec plusieurs conditions
age = 21
height = 178
age == 21 or height == 175 # La première condition est vraie, la seconde est fausse
# Retournera True puisqu'une des 2 conditions est vraie
```
- Avec l'opérateur `and`, il faut que les deux conditions soient vraies sinon l'ensemble ne le sera pas :

```py
# Exemple avec une seule condition
True and False # Donnera False parce qu'un des 2 termes est faux
```
- Autre exemple

```py
# Exemple avec plusieurs conditions
age = 21
height = 178
age == 21 and height == 178 # La première condition est vraie et la seconde l'est aussi. (True and True)
# Retournera True puisque les 2 conditions sont vraies.
```
- L'opérateur `not` ne fait qu'inverser l'état d'une condition

```py
is_boolean = True # Vraie
not is_boolean # Devient Faux
```
- Autres exemples
```py
not False # Devient Vrai

```
## 6-Tableau résumé

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

| A | `not A` |
|---|---|
| `True` | `False` |
| `False` | `True` |

## 7-Les structures de contrôle
En programmation, selon l'état d'une condition, certaines actions devraient être enclenchées et d'autres non. Pour ce faire on utilise ce qu'on appelle les structures de contrôle `if-elif-else`. Elles sont composées comme suit :
- Avec `if` `else`:

```py
if (condition): # Donc on commence par le if, ensuite dans la parenthèse on met la condition qu'on veut vérifier, puis on termine la ligne par un deux points (:)
    #Code à exécuter     # On indente pour que le programme comprenne ce qu'il doit exécuter selon la validité de la condition
else:                    # On indente ensuite le else au même niveau que le if et on termine la ligne par 2 points
    #Code à exécuter     # On indente pour que le programme comprenne ce qu'il doit exécuter selon la validité de la condition   

```
- Avec un `elif`

```py
if (condition): # Donc on commence par le if, ensuite dans la parenthèse on met la condition qu'on veut vérifier, puis on termine la ligne par un deux points (:)
    #Code à exécuter     # On indente pour que le programme comprenne ce qu'il doit exécuter selon la validité de la condition
elif (condition):        # On indente ensuite le elif au même niveau que le if et on spécifie la condition avant de terminer par 2 points (:)
    #Code à exécuter
else:                    # On indente ensuite le else au même niveau que le if et on termine la ligne par 2 points
    #Code à exécuter     # On indente pour que le programme comprenne ce qu'il doit exécuter selon la validité de la condition   

```

- Voici un exemple avec une condition simple
```py
age = 21
if (age >= 18):
    print("L'utilisateur est un adulte")
else:
    print("L'utilisateur n'est pas un adulte")
# Affichera donc que l'utilisateur est un adulte dans ce cas-ci
```
- Voici un exemple avec plusieurs conditions et opérateurs logiques ou comparatifs

```py
# (Ce n'est qu'un exemple subjectif, à ne pas prendre trop au sérieux)
taille = int(input("Veuillez saisir votre taille (en cm) : "))
if taille <= 0:
    dimension = "inexistante"
elif taille <= 165:
    dimension = "petite"
elif taille <= 180:
    dimension = "moyenne"
else:
    dimension = "grande"
print("L'utilisateur est de taille : " + dimension + ".")
```

## 8-Les structures de contrôle (imbriquées)
Il est également possible de mettre des structures à l'intérieur de structure de contrôle pour enchainer une succession de vérification de condition :

```py
# Exemple de la machine à billet d'attraction, pris du cours de Python d'Angela Yu 
# (https://www.udemy.com/course/100-days-of-code/) :
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and  age <= 55:
        print("You are free to ride the rollercoaster! (Because of your midlife crisis.)")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        if age >=45 and age <= 55:
            bill = 0
        else:
            bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


```