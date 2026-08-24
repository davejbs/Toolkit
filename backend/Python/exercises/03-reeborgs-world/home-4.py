# Ce code utilise des commandes spécifiques à l'environnement Reeborg's World
# (repeat, move(), turn_left(), etc.) les avertissements ou erreurs de l'éditeur sont normaux,
# ce n'est pas du Python standard exécutable ailleurs.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
...
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def l_shape():
    repeat 3:
        move()
    turn_left()
    repeat 3:
        move()
        
def next_L():
    turn_right()
    move()
    turn_right()

for step in range(3):
    l_shape()
    next_L()
l_shape()    