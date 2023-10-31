
"""
Exercice : création d'un QCM
"""
# score = 0
 
questionnaire1 = [
    {
        "titre": "L'art de cultiver des bonsaïs est originaire de ?",
        "reponses": [
            ("d'Afrique", False),
            ("d'Indonésie", False),
            ("du Japon", True)
        ]
    },
    {
        "titre": "Quelle est la capitale de la Belgique ?",
        "reponses": [
            ("Paris", False),
            ("Bruxelles", True),
            ("Stockholm", False)
        ]
    }
]


def derouler_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        print()
        print(question["titre"])
        reponses = question["reponses"]
        index = 1
        for reponse in reponses:
            print("Réponse " + str(index) + " = " + reponse[0])
            index += 1
        print("----------------")
        choix = input("Quelle est votre réponse ? ")
        choix_int = int(choix)
        if 0 < choix_int <= len(reponses):
            reponse_choisie = reponses[choix_int-1]
            if reponse_choisie[1]:
                print("Bonne réponse")
                score += 1
            else:
                print("Mauvaise réponse")
            print()
    return score

def quitter():  # création d'une fonction pour quitter le jeu
    quitt = ""
 
    while quitt != "o":
        quitt = input("Etes-vous sûr de vouloir quitter le jeu ? o/n ")
 
        if quitt == "o":
            print("Au revoir")
        elif quitt == "n":
            jeu_lancer()
        break
 
 
def jeu_lancer():
    choix = ""
 
    while choix != "o":
        global score
        choix = input("Are you ready ? o/n ")
        print("")
        if choix == "o":
            s = derouler_questionnaire(questionnaire1)
            print(f"Votre score est de {s}")
            re_jouer()
        elif choix == "n":
            quitter()
            break
        else:
            print("Veuillez répondre par o ou n !")
 
 
def re_jouer():
    jouer = ""
 
    while jouer != "o":
        jouer = input("Voulez-vous re-jouer ? o/n ")
        print("")
        if jouer == "o":
            jeu_lancer()
        elif jouer == "n":
            print("Merci d'avoir joué ... A bientôt ")
            break
 
 
print("")
print("Bienvenue dans ce jeu de questions à choix multiple.")
print()
 
jeu_lancer()
print("")

#derouler_questionnaire(questionnaire1)
