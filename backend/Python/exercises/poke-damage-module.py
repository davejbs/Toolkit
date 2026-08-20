charmander = {
    "attaque" : 52,
    "défense" : 43,
    "type" : "Feu"
}
bulbasaur = {
    "attaque" : 49,
    "défense" : 49,
    "type" : "Plante",
    "type2" : "Poison"
}

import random
def calcul_dégats(attaquant, défenseur, puissance):
    aléatoire = random.uniform(0.85, 1.0)
    ratio = attaquant / défenseur
    return ratio * puissance * aléatoire


dégats = calcul_dégats(charmander["attaque"], bulbasaur["défense"],40)
print(dégats)