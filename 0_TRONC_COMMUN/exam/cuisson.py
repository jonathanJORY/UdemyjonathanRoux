"""Chrono cuisson"""

import time

import winsound
FREQUENCE = 2500  # Set Frequency To 2500 Hertz
DUREE = 500  # Set Duration To 1000 ms == 1 second


# mode de cuisson, temps de cuisson min , sec
CUISSONS = (
    ("Test", 1, 2),
    ("Oeufs à la coque", 3, 0),
    ("Oeufs molet", 6, 0),
    ("Oeufs dur", 9, 0)
)

def affichage_temps(entrer):
    """
    Il imprime un point toutes les secondes, et toutes les 10 secondes il imprime le temps restant

    :param entrer: une liste de deux éléments, le premier étant le mode de cuisson,
    le second étant le
    temps de cuisson en minutes
    """
    temps_tot_seconde = entrer[1]*60+entrer[2]

    print(f"Cuisson d'{entrer[0]} en cours:")
    print("\nDuree restante:\n")
    for i in range(temps_tot_seconde, 0, -1):
        #minutes = temps_rest_seconde//60
        #sec = temps_rest_seconde%60
        minutes, sec = divmod(i, 60)
        print(f"{minutes}:{sec:02d}", end="\r")
        # end = le print ne se termine pas | flush affiche à chaque passage
        time.sleep(1)

def demander_valeur_numerique_utilisateur(valeur_max):
    """
    Il demande à l'utilisateur un nombre entre deux valeurs,
    et si l'utilisateur n'entre pas un nombre
    entre ces deux valeurs, il demande à nouveau

    :param valeur_min: La valeur minimale que l'utilisateur peut entrer
    :param valeur_max: La valeur maximale que l'utilisateur peut entrer
    :return: la valeur de v_int.
    """
    valeur_str= input(f"Donnez une valeur entre 1 et {valeur_max} : ")
    try:
        v_int = int(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_utilisateur(valeur_max)

    if not 1 <= v_int <= valeur_max:
        print(f"ERREUR : Votre valeur doit être entre 1 et {valeur_max}")
        return demander_valeur_numerique_utilisateur(valeur_max)

    return v_int

# Menu : choix cuisson

def main():
    """
    Il affiche un menu d'options de conversion, demande à l'utilisateur d'en choisir une,
    puis demande à l'utilisateur une valeur à convertir
    """
    print("\n-----------------")
    print("Cuisson des Oeufs")
    print("-----------------")
    i = 1
    for (mode, minutes, secondes) in CUISSONS:
        print(f"{i} - {mode} temps necessaire: {minutes}min {secondes:02d}")
        i += 1
    print(f"{i} - Quitter")

    choix_int = demander_valeur_numerique_utilisateur(i)
    if choix_int != len(CUISSONS)+1:
        affichage_temps(CUISSONS[choix_int-1])
        winsound.Beep(FREQUENCE, DUREE)
    print("Fin du programme")
main()
