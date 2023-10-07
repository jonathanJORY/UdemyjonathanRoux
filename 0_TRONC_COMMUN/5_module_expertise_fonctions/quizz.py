"""Quizz utilisation variable global"""


SCORE = 0
NB_QUESTIONS = 0
def poser_question(question, rep1, bonne_reponse):
    """
    Il pose une question, et si la réponse est correcte, il en ajoute un au score

    :param question: la question a se poser
    :param rep1: une liste de chaînes, les réponses possibles
    :param bonne_reponse: l'index de la bonne réponse dans la liste des réponses
    """
    global NB_QUESTIONS
    global SCORE
    NB_QUESTIONS += 1
    good = False
    while good is False:
        print("score:", SCORE)
        print("QUESTION")
        print("  " + question)
        for i in range(len(rep1)):
            print(f"   ({i+1}) {rep1[i]}")
        print()
        try:
            reponse = int(input("Votre réponse : "))
            good = True
        except ValueError:
            print("ERREUR: Entrer un numéro de réponse")
    if reponse == bonne_reponse:
        print("Bonne réponse")
        SCORE += 1
    else:
        print("Mauvaise réponse")
    print()


poser_question("Quelle est la capitale de la France ?", ["Marseille", "Nice", "Paris", "Nantes"], 3)
poser_question("Quelle est la capitale de l'Italie ?", ["Rome", "Venise", "Pise", "Florence"], 1)

print("Score final :", SCORE, "/", NB_QUESTIONS)
