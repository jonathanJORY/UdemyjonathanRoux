"""Jeu du bon nombre"""
import random


def demander_nombre(nb_min, nb_max):
    """
    Il demande à l'utilisateur d'entrer un nombre entre deux valeurs, et renvoie le nombre s'il est
    valide, ou redemande s'il ne l'est pas

    :param nb_min: le nombre minimum que l'utilisateur peut entrer
    :param nb_max: le nombre maximum que l'utilisateur peut deviner
    :return: le numéro que l'utilisateur a saisi.
    """
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

VIES = NB_VIES
GAGNE = False
i = 0
while not GAGNE and VIES > 0:
    VIES = NB_VIES-i
    print(f"Il vous reste {VIES} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        GAGNE = True
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")
    i +=1
if not GAGNE:
    print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")
