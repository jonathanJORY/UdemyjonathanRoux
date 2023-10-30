#          EtreVivant            ## Classe parent
#      Chat         Personne     ## Classes enfant (classes dérivées)
class EtreVivant:
    ESPECE_ETRE_VIVANT = "(être vivant non identifié)"

    def afficher_espece(self):
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"
    def __init__(self, nom_facultatif="inconnu"):
        self.nom = nom_facultatif

    def afficher_infos(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)


class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)"   # variable de classe (1 pour toutes les Personnes)

    def __init__(self, nom: str="", age: int=0, genre: bool=True):
        self.nom = nom
        self.age = age
        self.genre = genre
        if nom == "":
            self.demander_nom()
        if age == 0:
            self.demander_age()

    def __str__(self):
        return self.nom + " agé de : "+str(self.age)+" ans."
    
    def afficher_infos(self):
        e_optionnel = "" if self.genre else "e"
        genre_str = "Masculin" if self.genre else "Féminin"
        majeur_str = "majeur" if self.est_majeur() else "mineur"
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans")
        print(f"Genre : {genre_str + e_optionnel}")
        print(f"Je suis {majeur_str + e_optionnel}\n")

    def demander_age(self):
        self.age = input(f"Bonjour {self.nom} quel est votre age ? ")

    def demander_nom(self):
        self.nom = input(f"Bonjour quel est votre nom ? ")

    def est_majeur(self):
        return self.age >=18
    


class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):
        # self.nom = nom   # crée une variable d'instance : nom
        # self.age = age
        super().__init__(nom, age)
        self.etudes = etudes

    def afficher_infos(self):  # surchargé la méthode afficher_infos
        super().afficher_infos()
        print("Je suis etudiant en " + self.etudes)

# --- UTILISATION ---
liste_personnes = [Personne("Jean", 30), 
                   Personne("Paul", 15),
                   Personne("Zoe", 20)]

# Personne.ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.afficher_infos()
    personne.afficher_espece()
    print()

chat1 = Chat()
chat1.afficher_infos()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.afficher_infos()  # Bonjour, je suis un chat et je m'appelle Garfield
chat2.afficher_espece()

etreVivant = EtreVivant()
etreVivant.afficher_espece()

etudiant = Etudiant("Marc", 22, "Ecole d'ingénieur informatique")
etudiant.afficher_infos()
etudiant.afficher_espece()