# Python - Le module Random

## Table des matières
- [1. Un module](#1-un-module)
- [2. Le module Random](#2-le-module-random)
- [3. La fonction random() vs la fonction uniform()](#3-la-fonction-random-vs-la-fonction-uniform)
  - [Résumé technique](#résumé-technique)
  - [Quand utiliser random() ?](#quand-utiliser-random-)
  - [Quand utiliser uniform(a, b) ?](#quand-utiliser-uniforma-b-)
---

## 1-Un module
Avant d'aller plus loin, il est important de savoir ce qu'est un module. Un module est un fichier Python (`.py`) qui contient du code réutilisable, comme des fonctions, des variables, des classes, le tout organisé autour d'une tâche ou d'un thème spécifique.

- On utilise les modules dans le code principale en les important :

```py
import random # Importe le module random (qu'on va aborder plus bas)
```
- Pour utiliser les fonctions, variables ou classes d'un module, on appelle le module, puis on met un point pour appeler la fonciton spécifique
```py
import random 
variable = random.fonction() #.fonction n'appartient pas au module random. Ce n'est que pour illustrer mes propos.
```
- Pour en savoir sur les modules, se référer directement à la documentation : https://docs.python.org/3/tutorial/modules.html

## 2-Le module Random
> Documentation : https://docs.python.org/3/library/random.html

Le module Random est le module de Python qui permet de générer des nombres aléatoires à partir de différentes fonctions. On y retrouve par exemples les fonctions suivantes :


- Pour générer des nombres aléatoires entiers : `randint(a,b)`(a et b servent de paramètres/indications) :

```py
import random
variable = random.randint(1, 10) #Génère un nombre aléatoire entre 1 et 10, les deux inclus
print(variable) # Peut afficher 1,2,3,4,5,6,7,8,9,10
```
Pour générer des nombres aléatoires décimaux, il existe 2 méthodes principales : 

- La première méthode : `random()` génère des nombres décimaux entre [0, 1[ (0 inclus et 1 exclu)

```py
import random
variable = random.random()
print(variable) #Peut afficher n'importe quelle valeur dans l'intervalle [0.0, 1.0[
```
On peut aussi l'utiliser pour calculer de plus grands nombres au dessus de 1, comme 10 en les multipliant par un coefficient :

```py
# Si on veut par exemple des nombres décimaux entre [0 et 10[, (0 inclu et 10 exclu), on ferait :
import random
variable = random.random() * 10
print(variable) # Peut afficher n'importe quelle valeur entre 0.0 (inclus) et 10.0 (exclu), jamais 10.0 pile
```
- La seconde méthode : `uniform()` génère des nombres décimaux entre les nombres qui lui est passé en paramètres, comme pour "randint()"
```py
import random
variable = random.uniform(0, 30)
print(variable) #Peut afficher plusieurs valeurs entre 0.0 et 30.0
```
- Il existe d'autres méthodes moins courantes mais il reste préférable d'aller consulter la documentation :
> Documentation : https://docs.python.org/3/library/random.html

## 3-La fonction random() vs la fonction uniform()
Ce sont toutes les deux des fonctions similaires, qui font quasi la même chose mais de manière différente. Selon certains cas, il est plus avantageux d'en utiliser un plutôt que l'autre.

### Résumé technique

| | `random()` | `uniform(a, b)` |
|---|---|---|
| Plage | `[0.0, 1.0[` (fixe) | `[a, b]` (personnalisable) |
| Usage typique | Probabilités (%) | Plage de nombres précise |
| Sous le capot | Fonction "brute" | Utilise `random()` en interne : `a + (b-a) * random.random()` |

### Quand utiliser `random()` ?

- **Tester une probabilité/pourcentage** (le cas le plus courant) :
```py
if random.random() < 0.25:  # 25% de chance
    print("Objet rare trouvé !")
```
- **Choisir parmi plusieurs résultats pondérés** (les tranches doivent additionner à 1.0) :
```py
r = random.random()
if r < 0.40:
    resultat = "épée"      # 40%
elif r < 0.75:              # 0.40 + 0.35
    resultat = "bouclier"  # 35%
else:
    resultat = "potion"    # 25% (le reste)
```
- **Servir de brique de base** pour des formules mathématiques/statistiques plus complexes (distributions, bruit procédural, etc.)
- **Performance ultra critique** dans des boucles avec des millions d'itérations (gain minime, cas rare)

### Quand utiliser `uniform(a, b)` ?

- **Générer un nombre décimal dans une plage précise et arbitraire**, pour plus de lisibilité :
```py
degats = random.uniform(10, 50)  # dégâts entre 10 et 50
```
- Chaque fois que le calcul manuel (`a + random.random() * (b-a)`) ajouterait un risque d'erreur ou nuirait à la clarté du code.

