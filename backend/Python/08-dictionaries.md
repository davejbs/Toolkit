# Python - Les dictionnaires

## Table des matières
- [1. Le dictionnaire](#1-le-dictionnaire)
- [2. Manipuler un dictionnaire](#2-manipuler-un-dictionnaire)
  - [2.1. Retourner des valeurs](#21-retourner-des-valeurs)
  - [2.2. Ajouter ou modifier des valeurs](#22-ajouter-ou-modifier-des-valeurs)
  - [2.3. Manipulation avec fonctions](#23-manipulation-avec-fonctions)
- [3. Des dictionnaires imbriqués dans des dictionnaires](#3-des-dictionnaires-imbriqués-dans-des-dictionnaires)
  - [3.1. Récupération de données dans une imbrication](#31-récupération-de-données-dans-une-imbrication)

---

## 1-Le dictionnaire
Le dictionnaire est une structure de données, contenant une clé (`key`) avec laquelle s'associe une valeur (`value`). Il permet donc de stocker différentes données tout comme une liste, mais de les catégoriser par clé.

- Pour créer un dictionnaire on utilise des accolades `{}`

```py
# On crée ici un dictionnaire vide
mon_dictionnaire = {}
```
- Pour y insérer des données on met d'abord la clé puis, séparé par un `:`, la valeur

```py
# On ajoute ici dans le dictionnaire une clé nommée nom et on y associe la valeur Dave
mon_dictionnaire = {"nom": "Dave"}
```
- Une clé n'est pas obligée d'être une chaîne de caractères. Elle peut aussi provenir du contenu d'une variable déjà déclarée, c'est la valeur de la variable qui devient la clé, pas la variable elle-même

```py
nombre = 0
mon_dictionnaire = {nombre: 15}
print(mon_dictionnaire) # Affiche {0: 15}, la clé est bien le nombre 0
```
- Il est possible de créer un dictionnaire avec plusieurs clés et valeurs

```py
mon_dictionnaire = {
    "nom": "Dave",
    "age": 21,
    "status": "Étudiant"
}
```
> Par convention, on place chaque clé et valeur sur une ligne à part et on les sépare par une virgule.

## 2-Manipuler un dictionnaire
Il est possible d'effectuer différents types de manipulation sur les dictionnaires.

### 2.1-Retourner des valeurs
Il est possible de retourner des valeurs dans le dictionnaire en faisant appel à la clé directement, un peu comme avec les listes.

```py
mes_infos = {
    "nom": "Dave",
    "age": 21,
    "status": "Étudiant"
}
# Si je veux retourner mon nom :
print(mes_infos["nom"])
```

### 2.2-Ajouter ou modifier des valeurs
On peut également modifier ou ajouter de nouvelles clés et valeurs en appelant le dictionnaire, en lui passant la clé entre crochets, avant d'y assigner la valeur souhaitée.

- Si la clé existe déjà, sa valeur sera simplement changée

```py
mon_dictionnaire = {
    "nom": "Dave",
    "age": 21,
    "status": "Étudiant"
}
print(mon_dictionnaire["nom"]) # Affiche "Dave"
mon_dictionnaire["nom"] = "Dada" # Change la valeur de la clé nom
print(mon_dictionnaire["nom"]) # Affiche "Dada"
```

- Si la clé n'existe pas, elle sera créée avec la valeur qu'on lui aura assignée

```py
mon_dictionnaire = {
    "nom": "Dave",
    "age": 21,
    "status": "Étudiant"
}

mon_dictionnaire["taille_en_cm"] = 175 # Ajoute une nouvelle clé avec sa valeur assignée
```

### 2.3-Manipulation avec fonctions
Il existe des fonctions natives aux dictionnaires afin d'effectuer certaines actions comme des ajouts, des suppressions, des modifications, etc.

> Documentation officielle : https://docs.python.org/3/library/stdtypes.html#dict

Prenons un dictionnaire de base pour illustrer chaque méthode :

```py
mon_dict = {"nom": "Dave", "age": 21}
```

| Fonction/Méthode | Description | Exemple |
|---|---|---|
| `.get(clé)` | Retourne la valeur d'une clé, sans erreur si elle n'existe pas (retourne `None` par défaut) | `mon_dict.get("nom")` retourne `"Dave"` |
| `.keys()` | Retourne toutes les clés du dictionnaire | `mon_dict.keys()` retourne `dict_keys(['nom', 'age'])` |
| `.values()` | Retourne toutes les valeurs du dictionnaire | `mon_dict.values()` retourne `dict_values(['Dave', 21])` |
| `.items()` | Retourne chaque paire clé-valeur sous forme de tuples | `mon_dict.items()` retourne `dict_items([('nom', 'Dave'), ('age', 21)])` |
| `.pop(clé)` | Retire une clé et retourne sa valeur | `mon_dict.pop("age")` retourne `21` et retire la clé |
| `.update(dict2)` | Ajoute une nouvelle paire clé-valeur si la clé n'existe pas encore | `mon_dict.update({"ville": "Montréal"})` ajoute la clé `ville` |
| `.update(dict2)` | Écrase la valeur d'une clé si elle existe déjà | `mon_dict.update({"nom": "Dada"})` remplace la valeur de la clé `nom` |
| `.update(dict2)` | Fusionne plusieurs paires en un seul appel (ajoute et/ou écrase selon chaque clé) | `mon_dict.update({"ville": "Montréal", "age": 22})` ajoute `ville` ET modifie `age` |
| `len(dict)` | Retourne le nombre de paires clé-valeur | `len(mon_dict)` retourne `3` |

> À noter : `mon_dict["clé_inexistante"]` lance une erreur (`KeyError`) si la clé n'existe pas, alors que `.get("clé_inexistante")` retourne simplement `None`, sans faire planter le programme.

> À noter également : `.update()` n'accepte qu'**un seul** dictionnaire par appel. `mon_dict.update({...}, {...})` avec deux arguments séparés lance une erreur (`TypeError`). Pour fusionner plusieurs sources, soit on les combine dans un seul dictionnaire avant de les passer, soit on appelle `.update()` plusieurs fois de suite.

## 3-Des dictionnaires imbriqués dans des dictionnaires
Tout comme pour les listes, il est possible d'imbriquer des dictionnaires à l'intérieur de dictionnaires, ou des listes à l'intérieur de dictionnaires.


```py
dictionnaire = {
    "info_Dave": {
        "nom": "Dave",
        "age": 21,
        "loisirs": ["nourriture", "musique"]
    },
    "infos_Dada": {
        "nom": "Dada",
        "age": 21
    }
}
```

### 3.1-Récupération de données dans une imbrication
Pour récupérer une information précise d'une imbrication, il suffit de placer les index l'un après l'autre directement (`dictionnaire[][]...`).

- Si je veux récupérer la donnée "musique" :

```py
dictionnaire = {
    "info_Dave": {
        "nom": "Dave",
        "age": 21,
        "loisirs": ["nourriture", "musique"]
    },
    "infos_Dada": {
        "nom": "Dada",
        "age": 21
    }
}
print(dictionnaire["info_Dave"]["loisirs"][1])
```