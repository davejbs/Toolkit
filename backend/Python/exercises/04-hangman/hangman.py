import random
import stage
import word_list

print(stage.logo)
# L'ordi choisi un mot aléatoirement à partir d'une liste
mot_choisi = random.choice(word_list.liste_mot)

# L'indicatif s'affiche pour donner le nombre de lettre dans le mot
indicatif = "_" * len(mot_choisi)
print(f"{indicatif} ({len(indicatif)} lettres)")

partie_terminée = False
lives = 6
lettres_découvertes = []
avancée_pendue = -1
lettres_essayées = []

# Invite l'utilisateur a saisir une lettre
while partie_terminée != True:
    tentative = str(input("Veuillez saisir une lettre : ")).lower()

    # Si l'utilisateur saisie une lettre déjà saisie
    while tentative in lettres_essayées:
        print(f"Vous avez déjà essayé cette lettre : {tentative}")
        tentative = str(input("Veuillez saisir une lettre : ")).lower()

    # Si l'utilisateur saisie plus d'une lettre :
    while len(tentative) > 1:
        print(f"Vous devez saisir une seule lettre à la fois :")
        tentative = str(input("Veuillez saisir une lettre : ")).lower()
    # Si l'utilisateur ne saisie rien :
    while len(tentative) == 0:
        print(f"Vous devez saisir au moins une lettre pour jouer :")
        tentative = str(input("Veuillez saisir une lettre : ")).lower()

    # Vérifie si la lettre fait parti du mot aléatoirement choisi, si oui l'affiche
    affichage = ""
    for lettre in mot_choisi:
        if tentative == lettre:
            affichage += lettre
            lettres_découvertes.append(lettre)
        elif lettre in lettres_découvertes:
            affichage += lettre    
        else:
            affichage += "_"  
    lettres_essayées.append(tentative)        
    print(affichage)

    # Conséquence si la tentative ne correspond pas à une lettre du mot : 
    if tentative not in mot_choisi:
        lives -= 1
        print(f"La lettre {tentative} ne fait pas partie du mot. Vous perdez une vie")
        avancée_pendue -= 1
        print(f"Il vous reste : {lives} vies.")

    print(stage.stages[avancée_pendue])
    print(f"Lettres déjà essayées : {' - '.join(lettres_essayées)}")

    # Condition de fin de jeu
    if "_" not in affichage:
        partie_terminée = True
        print(f"Félicitation vous avez trouvé le mot : {mot_choisi}")

    if lives == 0:
        partie_terminée = True
        print(f"Dommage, vous avez perdu... Le mot était : {mot_choisi}")

