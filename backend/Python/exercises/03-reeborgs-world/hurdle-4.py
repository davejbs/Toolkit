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
    
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    

    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    