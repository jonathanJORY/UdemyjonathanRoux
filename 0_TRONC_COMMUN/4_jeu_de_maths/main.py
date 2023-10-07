"""Module random jeu calcul"""
import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 10


def poser_question():
    """
    It asks a random math question, and returns True if the answer is correct, and False otherwise
    :return: True or False
    """
    nb_aleatoire_un = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nb_aleatoire_deux = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    operateur = random.randint(0, 1)
    operateur_str = "+"
    calcul = nb_aleatoire_un+nb_aleatoire_deux
    if operateur == 1:
        operateur_str = "*"
        calcul = nb_aleatoire_un*nb_aleatoire_deux
    reponse_str = input(f"Calculez: {nb_aleatoire_un} {operateur_str} {nb_aleatoire_deux} = ")
    reponse_int = int(reponse_str)
    if reponse_int == calcul:
        return True
    return False


POINTS = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}:")
    if poser_question():
        print("Réponse correcte")
        POINTS += 1
    else:
        print("Réponse incorrecte")
    print()

# Votre note est 2/4
print(f"Votre note est : {POINTS} / {NB_QUESTIONS}")

MOYENNE = int(NB_QUESTIONS/2)

if POINTS == NB_QUESTIONS:
    print("Excellent!")
elif POINTS == 0:
    print("Révisez vos maths!")
elif POINTS > MOYENNE:
    print("Pas mal!")
else:
    print("Peut mieux faire")
