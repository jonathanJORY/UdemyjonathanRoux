# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

class Question:
    num_question = 0
    def from_data(data):
        q = Question(data[2], data[0],data[1])
        return q
    def __init__(self, titre: str, choix, bonne_rep: str):
        self.num_question += 1
        self.titre = titre
        self.choix = choix
        self.bonne_rep = bonne_rep
        self.numero = self.num_question

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)

    def poser_question(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_rep.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

class Questionnaire:
    score = 0
    def __init__(self, titre: str, questions):
        self.titre = titre
        self.questions = questions

    def lancer_questionnaire(self):
        for question in self.questions:
            if question.poser_question():
                self.score += 1
        print("Score final :", self.score, "sur", len(self.questions))


data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris",
        "Quelle est la capitale de la France ?")


questionnaire1 = Questionnaire("test",(
    Question("Quelle est la capitale de la France ?",
             ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?",
             ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?",
             ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"),
    Question.from_data(data)
            ),
        )

questionnaire1.lancer_questionnaire()

