import caesar_art
from caesar_caractères import alphabet

# Fonction pour chiffrer ou déchiffrer
def caesar(choix, message_original, clé_chiffrement_déchiffrement):
    message_modifié = ""
    if choix == "déchiffrer":
        clé_chiffrement_déchiffrement *= -1    
    for lettre in message_original:
        if lettre in alphabet:
            position_lettre = alphabet.index(lettre)
            nouvelle_position_lettre = position_lettre + clé_chiffrement_déchiffrement
            message_modifié += alphabet[nouvelle_position_lettre % len(alphabet)]
            # Cette ligne s'assure que la boucle ne sort jamais de la limite en utilisant le modulo
        else:
            message_modifié += lettre
    print(f"Votre message modifié est : {message_modifié}.")
        
    
print(caesar_art.logo)

# Boucle le programme aussi longtemps que le souhaite l'utilisateur
programme_actif = True

while programme_actif == True:
    option = input("Tapez 'chiffrer' pour chiffrer un message, tapez 'déchiffrer' pour déchiffrer un message:\n").lower()
    while option != "chiffrer" and option != "déchiffrer":
        print("Veuillez choisir l'une des deux options suivantes s'il vous plait :")
        option = input("Tapez 'chiffrer' pour chiffrer un message, tapez 'déchiffrer' pour déchiffrer un message:\n").lower()

    # Demande à l'utilisateur de saisir ces informations
    message = input("Tapez votre message:\n").lower()
    clé_numérique = int(input("Tapez un nombre pour définir le numéro de cryptage:\n"))
    caesar(option, message, clé_numérique)
    continuer_programme = str(input("Tapez 'oui' si vous souhaitez utiliser le programme à nouveau. Sinon, tapez 'non': ")).lower()

    # Demande à l'utilisateur s'il souhaite continuer à utiliser le programme    
    while continuer_programme != "oui" and continuer_programme != "non":
        print("Veuillez choisir l'une des deux options suivantes s'il vous plait :")
        continuer_programme = str(input("Tapez 'oui' si vous souhaitez utiliser le programme à nouveau. Sinon, tapez 'non': ")).lower()
    if continuer_programme == "non":
        programme_actif = False
