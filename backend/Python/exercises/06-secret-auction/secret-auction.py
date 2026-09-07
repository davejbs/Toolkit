from display_utils import logo, clear

print(logo)
offres_enchères = {}
continuer_programme = True

def comparer():
    offres = offres_enchères.values()
    meilleure_offre = max(offres)
    gagnant_enchère = []

    for clé in offres_enchères:
        if offres_enchères[clé] == meilleure_offre:
            gagnant_enchère.append(clé)
    if len(gagnant_enchère) > 1:
        gagnants_enchères = " - ".join(gagnant_enchère)
        print(f"Il y a égalité parmi {gagnants_enchères} pour des offres de {meilleure_offre}. Les gagnants doivent refaire une enchère entre eux.")
    else:
        gagnant_enchère = "".join(gagnant_enchère)
        print(f"Le gagnant de l'enchère est: {gagnant_enchère} avec une offre de: {meilleure_offre}. Félicitation!")


# TODO-1: Ask the user for input
while continuer_programme == True:
    nom = str(input("Quel est votre nom ?: "))
    offre = int(input("Quelle est votre enchère?: "))

    # TODO-2: Save data into dictionary {name: price}
    offres_enchères.update({nom : offre})

    # TODO-3: Whether if new bids need to be added
    continuer = str(input("Est-ce qu'il y a d'autres offrants? Tapez 'oui' ou 'non': ")).lower()
    while continuer != "oui" and continuer != "non":
        print("Veuillez s'il vous plait choisir l'un des deux options demandées")
        continuer = str(input("Est-ce qu'il y a d'autres offrants? Tapez 'oui' ou 'non': ")).lower()

    if continuer == "non":
        continuer_programme = False
    clear()    

# TODO-4: Compare bids in dictionary
comparer()
