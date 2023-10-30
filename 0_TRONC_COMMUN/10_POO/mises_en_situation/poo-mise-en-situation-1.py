# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        # Affiche le message de présentation de la personne
        e_optionnel = "" if self.genre else "e"
        genre_str = "Masculin" if self.genre else "Féminin"
        majeur_str = "majeur" if self.EstMajeur() else "mineur"
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans")
        print(f"Genre : {genre_str + e_optionnel}")
        print(f"Je suis {majeur_str + e_optionnel}\n")

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()