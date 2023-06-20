import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print(f"ERREUR: vous devez entrer un nombre. Réessayez")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: vous devez rentrer un nombre valide (entre {nb_min} et {nb_max}). Réessayez")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

nombre = 0
vies = NB_VIES

while nombre != NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vie(s)")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre < NOMBRE_MAGIQUE:
        print("Le nombre est plus grand")
        vies -= 1
    else:
        print("Le nombre est plus petit")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu, le nombre magique était {NOMBRE_MAGIQUE}")