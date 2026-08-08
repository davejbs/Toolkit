# Python - Les opérations mathématiques

## Table des matières
- [1. Les opérateurs mathématiques](#1-les-opérateurs-mathématiques)
- [2. Les opérateurs d'assignation](#2-les-opérateurs-dassignation)
- [3. L'ordre de priorité des opérations (PEMDAS)](#3-lordre-de-priorité-des-opérations-pemdas)
--- 

## 1-Les opérateurs mathématiques
Les opérateurs sont des symboles qui sont en réalité des fonctions permettant d'effectuer un type d'opération spécifique. On retrouve par exemple les cas classiques :

| Opérateur | Nom | Exemple | Résultat |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (retourne un float, même si le résultat est propre) | `10 / 2` | `5.0` |
| `//` | Division entière (retourne le résultat arrondi vers le bas, en type int) | `10 // 3` | `3` |
| `**` | Exposant | `5 ** 2` | `25` |

Mais également des cas spécifiques comme :

| Opérateur | Nom | Exemple | Résultat |
|---|---|---|---|
| `%` | Modulo (retourne le reste d'une division) | `10 % 3` | `1` |


## 2-Les opérateurs d'assignation

Les opérateurs d'assignation combinent une opération mathématique avec une affectation (`=`). Il est possible de les utiliser sous 2 formes, la forme raccourcie ou la forme complète.

| Forme raccourcie | Forme complète |
|---|---|
| `x += valeur` | `x = x + valeur` |
| `x -= valeur` | `x = x - valeur` |
| `x *= valeur` | `x = x * valeur` |
| `x /= valeur` | `x = x / valeur` |
| `x //= valeur` | `x = x // valeur` |
| `x **= valeur` | `x = x ** valeur` |
| `x %= valeur` | `x = x % valeur` |

## 3-L'ordre de priorité des opérations (PEMDAS)

Comme en mathématiques, Python respecte un ordre de priorité précis entre les opérateurs. Les parenthèses permettent toujours de forcer l'ordre voulu.

| Priorité | Opérateur(s) | Nom |
|---|---|---|
| 1 (la plus haute) | `()` | Parenthèses |
| 2 | `**` | Exposant |
| 3 | `*`, `/`, `//`, `%` | Multiplication, division, division entière, modulo |
| 4 (la plus basse) | `+`, `-` | Addition, soustraction |

> À priorité égale (ex : `*` et `/` ensemble), Python évalue de gauche à droite.