"""Jeu du simon, retener la séquence"""
import os
import time
import random

# niveau str, temps attente, nb départ, vies

NIVEAU = (
    {
    "titre": "Facile",
    "temps_mémo": 5,
    "init_seq": 2,
    "nb_essaie": 3
    },
    {
    "titre": "Normal",
    "temps_mémo": 3,
    "init_seq": 3,
    "nb_essaie": 2
    },
    {
    "titre": "Difficile",
    "temps_mémo": 1,
    "init_seq": 4,
    "nb_essaie": 1
    }
)
ATTENTE_CLASSIQUE = 3

def clear_screen():
    """
    efface l'écran duivant l'os
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def choix_niveau(difficulte):
    """
    Il prend un tuple de dictionnaires comme argument,
    imprime le contenu de chaque dictionnaire du
    tuple, demande à l'utilisateur de choisir l'un des dictionnaires
    renvoie le dictionnaire choisi

    :param difficulte: [{'titre', 'temps_mémo', 'nb_essaie'}
    :return: le dictionnaire du niveau choisi par l'utilisateur.
    """
    print("Choix du niveau :")
    index = 1
    for elem in difficulte:
        print(f""" - {index} : Niveau: {elem['titre']}
       temps d'attente: {elem['temps_mémo']}s
       vies: {elem['nb_essaie']} \n""")
        index +=1
    try:
        val_int = int(input("Quel niveau choisis-tu ? "))
    except ValueError:
        print("\nERREUR : Vous devez rentrer une valeur numérique\n")
        return choix_niveau(difficulte)

    if not 1 <= val_int <= len(difficulte):
        print(f"\nERREUR : Votre valeur doit être entre 1 et {len(difficulte)}\n")
        return choix_niveau(difficulte)
    clear_screen()

    return difficulte[val_int-1]


def main():
    """
    Il imprime la séquence de nombres et demande ensuite à l'utilisateur d'entrer la séquence.
    Si l'utilisateur saisit la bonne séquence,
    le score est incrémenté de 1 et la séquence est incrémentée
    de 1. Si l'utilisateur saisit la mauvaise séquence, le nombre de vies est décrémenté de 1.
    Si le nombre de vies est inférieur à 1, le le jeu est fini.
    """
    score = 0
    sequence = ""
    niveau_entrer_dict = choix_niveau(NIVEAU)
    nb_essaies_restant = niveau_entrer_dict['nb_essaie']
    print(f"Niveau {niveau_entrer_dict['titre']}, Bonne chance")
    time.sleep(ATTENTE_CLASSIQUE)
    for _ in range(niveau_entrer_dict['init_seq']):
        sequence += str(random.randint(0, 9))
    while True:
        clear_screen()
        print("Retenez la séquence")
        time.sleep(1)
        print(sequence)
        time.sleep(niveau_entrer_dict['temps_mémo'])
        clear_screen()
        entree = input("Votre réponse : ")
        if entree == sequence:
            score += 1
            print("Bonne réponse, votre score est de :",score)
            sequence += str(random.randint(0, 9))
        else:
            print("Mauvaise réponse")
            time.sleep(ATTENTE_CLASSIQUE)
            if nb_essaies_restant < 1:
                print(f"""Vous avez perdu, la séquence était : {sequence},
                votre score final est : {score}""")
                break
            nb_essaies_restant -= 1
            print(f"Il vous reste {nb_essaies_restant} vie(s) attention")
        time.sleep(ATTENTE_CLASSIQUE)


main()
