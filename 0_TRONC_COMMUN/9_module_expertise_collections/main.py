""" LES FONCTIONS : PROJET QUESTIONNAIRE"""

def demande_reponse(minimum, maximum):
    """
    La fonction « demande_reponse » invite l'utilisateur à saisir un nombre compris entre une valeur
    minimale et maximale, et continue de demander jusqu'à ce qu'un nombre valide dans la plage soit
    saisi.

    :param minimum: Le paramètre minimum représente la valeur minimale que doit être la réponse de
    l'utilisateur. Il s'agit de la limite inférieure de la plage des valeurs acceptables
    :param maximum: Le paramètre maximum représente la limite supérieure de la plage de valeurs que
    l'utilisateur peut saisir
    :return: la réponse de l'utilisateur, qui est un nombre entier compris entre les valeurs
    minimale et maximale spécifiées.
    """
    reponse = 0
    while reponse < minimum or reponse > maximum:
        reponse = input(f"Votre réponse entre: {minimum} et {maximum}: ")
        try:
            reponse = int(reponse)
        except ValueError:
            print("Veuillez entrer un nombre entier. Réessayez.\n")
            reponse = 0
        if reponse > maximum:
            print("Valeur non comprise entre",minimum, "et", maximum, ". Réessayez.\n")
    return reponse


def recurcive_demande_reponse(minimum, maximum):
    """
    La fonction « demande_reponse » invite l'utilisateur à saisir un nombre compris entre une valeur
    minimale et maximale, et continue de demander jusqu'à ce qu'un nombre valide dans la plage soit
    saisi.

    :param minimum: Le paramètre minimum représente la valeur minimale que doit être la réponse de
    l'utilisateur. Il s'agit de la limite inférieure de la plage des valeurs acceptables
    :param maximum: Le paramètre maximum représente la limite supérieure de la plage de valeurs que
    l'utilisateur peut saisir
    :return: la réponse de l'utilisateur, qui est un nombre entier compris entre les valeurs
    minimale et maximale spécifiées.
    """
    reponse = 0
    reponse = input(f"Votre réponse entre: {minimum} et {maximum}: ")
    try:
        reponse = int(reponse)
    except ValueError:
        print("Veuillez entrer un nombre entier. Réessayez.\n")
        reponse = recurcive_demande_reponse(minimum, maximum)
    if reponse > maximum:
        print("Valeur non comprise entre",minimum, "et", maximum, ". Réessayez.\n")
        reponse = recurcive_demande_reponse(minimum, maximum)
    return reponse

def poser_question(question):
    """
    La fonction `poser_question` prend une question en entrée, affiche la question et ses options,
    demande à l'utilisateur une réponse, vérifie si la réponse est correcte, met à jour le SCORE et
    imprime le résultat.

    :param question: Le paramètre « question » est une liste qui contient les éléments suivants :
    """
    res = False
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(question[1])):
        print(f" {i+1} - " + question[1][i])
    print()
    int_reponse = recurcive_demande_reponse(1, len(question[1]))
    if question[1][int_reponse-1].lower() == question[2].lower():
        print("Bonne réponse")
        res = True
    else:
        print("Mauvaise réponse")

    print()
    return res

def lancer_questionnaire(questionnaire):
    """
    La fonction `lancer_questionnaire` prend une liste de questions en entrée, affiche chaque
    question et ses options, demande à l'utilisateur une réponse, vérifie si la réponse est
    correcte, met à jour le SCORE et imprime le résultat.

    :param questionnaire: Le paramètre « questionnaire » est une liste qui contient des questions
    sous forme de listes.
    """
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("SCORE final :", score)


questionnaire= (("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"),
             "Paris"),
             ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"),
             "Rome"))

lancer_questionnaire(questionnaire)
