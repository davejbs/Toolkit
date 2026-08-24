# Ce code utilise des commandes spécifiques à l'environnement Reeborg's World
# (repeat, move(), turn_left(), etc.) les avertissements ou erreurs de l'éditeur sont normaux,
# ce n'est pas du Python standard exécutable ailleurs.

# Pour cet exercice spécifiquement, j'ai utilisé la règle de la main droite. Une astuce pour
# terminer n'importe quel labyrinthe est de toujours garder la droite. C'est ce que fera le
# robot en priorisant systématiquement un virage à droite quand c'est possible.

def turn_right():
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
