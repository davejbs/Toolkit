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
    
def turn_arround():
    turn_left()
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    elif not front_is_clear():
        while wall_in_front() and not right_is_clear():
            turn_left()
    move()
