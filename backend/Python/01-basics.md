# Python - Les bases

## Table des matières
- [1. Les variables et types de données](#1-les-variables-et-types-de-données)
- [2. La saisie de données](#2-la-saisie-de-données)
- [3. L'affichage de données](#3-laffichage-de-données)
--- 
## 1-Les variables et types de données

### Les variables 
Les variables permettent de stocker et de manipuler des données. 

### Les types de données 
Il existe 4 types de variables : string, int, float et booléen
```py
role = "Utilisateur" # Variable nommée role contenant une chaîne de caractères
age = 21 # Variable nommée age contenant un nombre entier
prix = 20.00 # Variable nommée prix contenant un nombre décimal
is_boolean = True # Variable nommée is_boolean contenant un booléen de valeur True
```
> Convention : en Python, les variables se nomment en **snake_case** (ex: `is_boolean`), pas en camelCase — peu importe leur type.
- Il est possible de connaître le type d'une variable avec la fonction `type()` : 
```py
age = 21
type(age) # Retourne le type de la variable (ici un int)
```
### La conversion de type des données 
Il est possible de changer le type des données, à la mesure de la logique.

- `str()` : Permet de changer une donnée en chaîne de caractères :
```py
nombre = 21
nombre = str(nombre)
print(nombre) # Affiche 21 (En texte même si la différence n'est pas très visible)
```
- `int()` : Permet de changer une donnée en nombre entier (non, ça ne marchera pas avec des lettres) : 
```py
age = 21.0
age = int(age)
print(age) # Affiche 21
```

- `float()` : Permet de changer une donnée en nombre décimal : 
```py
prix = 20
prix = float(prix)
print(prix) # Affiche 20.0
```
- `bool()` : Permet de changer une donnée en booléen. : 
```py
print(bool("")) # False -> une chaîne vide est "falsy"
print(bool("False")) # True -> étonnamment ! Toute chaîne non-vide est "truthy", peu importe son contenu
print(bool(0)) # False
print(bool(1)) # True
```


## 2-La saisie de données

### La fonction `input()`
Permet à un utilisateur de saisir une donnée, puis de la stocker 
- Cas d'utilisation #1 : Saisie d'une donnée et de la capturer dans une variable
- Si le type d'input n'est pas précisé, peu importe ce que l'utilisateur saisit, ce sera automatiquement de type chaîne de caractères 

```py
variable = input("Une invite pour l'utilisateur") # Ce que saisiera l'utilisateur sera enregistrée dans la variable
# C'est aussi possible de l'utiliser dans le vide mais si ce que l'utilisateur a saisi n'est enregistrée nulle part, cela ne sert à rien.
```

- Cas d'utilisation #2 : Input avec un type spécifique : 
```py
variable_int = int(input("Saisir un nombre entier.")) # La donnée entrée devra donc être de type int, sinon une erreur sera levée
variable_float = float(input("Saisir un nombre décimal")) # La donnée entrée devra donc être de type float sinon une erreur sera levée
variable_str = str(input("Saisir une chaîne de caractères")) # Sauf qu'ici c'est totalement redondant et inutile étant donné le cas d'utilisation #1
variable_bool = bool(input("Veuillez taper quelque chose")) # Si l'utilisateur entre une donnée, la valeur sera vraie (chaîne non-vide = "truthy"), si l'utilisateur laisse vide, la valeur sera fausse (chaîne vide = "falsy")
```


## 3-L'affichage de données

### La fonction `print()`
Permet d'afficher des données dans la console.

- Cas d'utilisation #1 : Afficher une simple chaîne de caractères
```py
print("Hello World") # Affiche dans la console : Hello World 
```
- Cas d'utilisation #2 : Concaténation manuelle
```py
age = 21
print("L'utilisateur a :" + str(age) + " ans.") # Pour rappel : on convertit le contenu de la variable "age" en chaîne de caractères pour permettre la concaténation, sinon ça ne marchera pas.
```
- Cas d'utilisation #3 : Concaténation automatique en mettant "f" avant les guillemets et en utilisant {} (f-string)

```py
age = 21
print(f"L'utilisateur a : {age} ans.") # Python fait automatiquement les conversions de types, ça affichera dans le terminal : L'utilisateur a 21 ans.

# Il est aussi possible d'y concaténer des résultats :
print(F"Dans 5 ans, l'utilisateur aura : {age + 5} ans")
```
> À noter qu'on peut utiliser des f-string en écrivant f"" comme en écrivant F"" 
- Cas d'utilisation #4 : En intégrant des sauts de lignes avec `\n`

```py
print("Ce message sera\nsur 2 lignes")
```

- Cas d'utilisation #5 : Plusieurs données séparées par des virgules
- Il est également possible d'y ajouter en paramètre le séparateur `sep=""` (entre les guillemets on mets le caractère qui servira à séparer) 


```py
# Sans séparateur :
age = 21
nom = "Utilisateur"
print(nom, age) # Affichera dans la console : Utilisateur 21 

# Avec séparateur `sep=`:
age = 21
nom = "Utilisateur"
print(nom,age,sep=" - ") # Ici le séparateur est composé d'un espace, trait d'union et espace. La console affichera donc : Utilisateur - 21
```
- Cas d'utilisation #6 : Combiner avec d'autres méthodes : 

```py
age = 21
print(type(age)) # Affichera : <class 'int'>
```

- Cas d'utilisation #7 : Combiner avec un input(): 
```py
print("Hello " + input("Quel est votre nom ? :"))
# Si l'utilisateur saisit Dave, alors la console affichera : Hello Dave
# Même si cette approche est faisable, elle n'est pas recommandée en raison de la lourdeur de sa lisibilité
```
- Cas d'utilisation #8 : Afficher un message de plusieurs lignes (Un code en braille par exemple):
```py
print('''
⠀⠀⠀⠀⠀⢸⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠑⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠙⢤⡷⣤⣦⣀⠤⠖⠚⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡿⠢⢄⡀⠀⡇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠸⠷⣶⠂⠀⠀⠀⣀⣀⠀⠀⠀
⢸⣃⠀⠀⠉⠳⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢉⡭⠋
⠀⠘⣆⠀⠀⠀⠁⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀
⠀⠀⠘⣦⠆⠀⠀⢀⡎⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⣠⠔⠋⠀⠀⠀⠀
⠀⠀⠀⡏⠀⠀⣆⠘⣄⠸⢧⠀⠀⠀⠀⢀⣠⠖⢻⠀⠀⠀⣿⢥⣄⣀⣀⣀⠀⠀
⠀⠀⢸⠁⠀⠀⡏⢣⣌⠙⠚⠀⠀⠠⣖⡛⠀⣠⠏⠀⠀⠀⠇⠀⠀⠀⠀⢙⣣⠄
⠀⠀⢸⡀⠀⠀⠳⡞⠈⢻⠶⠤⣄⣀⣈⣉⣉⣡⡔⠀⠀⢀⠀⠀⣀⡤⠖⠚⠀⠀
⠀⠀⡼⣇⠀⠀⠀⠙⠦⣞⡀⠀⢀⡏⠀⢸⣣⠞⠀⠀⠀⡼⠚⠋⠁⠀⠀⠀⠀⠀
⠀⢰⡇⠙⠀⠀⠀⠀⠀⠀⠉⠙⠚⠒⠚⠉⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢧⡀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣶⣶⣿⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⢿⣳⠞⠳⡄⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠹⣄⣀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''') # Les triples guillemets permettent d'écrire du texte sur plusieurs lignes sans avoir besoin de \n
# Source : https://emojicombos.com/pokemon-ascii-art
```
- Cas d'utilisation #9 : Afficher du texte contenant des symboles particuliers : 
```py
print(r'''
Ce que ça fait de débugger du code :

  1- ＿〆(˘ᗜ˘)  - C'est parti pour une nouvelle session de code

  2- ＿φ(◦'⌣'◦) - Voyons voir, si j'écris ça et ça, ça devrait fonctionner

  3-_〆(･_･｡) - Oh, ça ne fonctionne pas, où est le bug (**commence à chercher** et le temps commence à passer**)

  4- ＿〆(。。)  **Cherche plus fort et encore plus de temps passe**

  5- ｡｡｡o(ﾟ^ ﾟ)Hmm... - Je ne comprends pas pourquoi ça ne fonctionne pas... Bon, allons voir sur Stack Overflow

  6- ＿φ(°-°=) - **Compare les codes** - Mais j'ai fait ça, pourquoi ça ne marche pas ? Attends...

  7- φ(｡_｡ *)  **Trouve le bug** - Oh, j'ai trouvé l'erreur ! La voilà !

  8- (ﾉ*'‐')ﾉ ﾐ ┸┸ - Oh wow, tout ça à cause d'une indentation mal placée

  9- (∩⌣̀_⌣́) - Argh, j'ai maintenant mal à la tête. Faut vraiment que j'arrête de coder dans notepad++. J'ai besoin d'une pause.
''')
# Source : https://emoticonhub.com/#google_vignette 
# Le "r" avant les triples guillemets crée une "raw string" : Python
# traite le \ littéralement plutôt que comme le début d'une séquence
# d'échappement (comme \n ou \t), ce qui évite les avertissements/erreurs.
```

