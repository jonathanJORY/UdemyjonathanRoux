# Comparer des objets
# is / == / isinstance

class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Predateur:
    def chasser_et_manger_proie(self):
        print("miam miam")

class Lion(EtreVivant, Predateur):
    def afficher_infos(self):
        print("Je suis un lion")

class Chat(EtreVivant):
    def afficher_infos(self):
        print("Je suis un chat")

class Personne(EtreVivant):
    TYPE = "Humain"

    def __init__(self, nom: str = "", age: int = 0, amis: list = []):
        self._test = ""  # accessible depuis l'intérieur et les classes enfants
        self.nom = nom  # public, accessible à l'intérieur et à l'extérieur
        self.__age = age  # private, utilisable uniquement à l'intérieur de la classe
        if not isinstance(age, int):
            print("L'age doit être de type int")
            self.__age = 0
        self.amis = amis

    def afficher_infos(self):
        print("Je suis une personne")

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.__age} ans")
        if self.__age > 0:
            print(f"L'an prochain j'aurai {self.__age+1}")

    def __str__(self):  # affichage du print
        return "Je m'appelle " + self.nom + ", j'ai " + str(self.__age) + " ans"

    def __eq__(self, other):  # tester l'égalité (equals en Java)
        return self.nom == other.nom and self.__age == other.__age

    def __repr__(self):  # représentation de l'objet
        return self.__class__.__name__ + " " + str(self.__dict__)

    # Méthode statique
    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print("Méthode de classe : " + cls.TYPE)

print(Personne.formater_chaine("toTo"))
Personne.methode_de_classe()

personne1 = Personne("Jean", 20, ["Claire", "Marc"])
personne1.AfficherInfos()

personne2 = Personne("Jean", 20, ["Claire", "Marc"])
personne2.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)
print(personne1.__dict__ == personne2.__dict__)

import copy

# COPIER DES OBJETS
# shallow copy / deep copy
personne2 = copy.copy(personne1)  # copy peut profonde copie différente personne mais même listes d'amis
personne1.amis[0] = "Chantale"  # personne2.amis[0] sera aussi modifié
personne1.nom = "toto"  # personne2.nom ne sera pas changé
# tandis que copy.deepcopy(personne1) recrée tout, même les listes (copie profonde)

# POLYMORPHISME
# Plusieurs types -> la même interface (même code)
l = [EtreVivant(), Chat(), Personne()]

for e in l:
    e.afficher_infos()

# ---------------------------------

def additionner(a, b):
    somme = 0
    if isinstance(a, int):
        somme += a
    if isinstance(a, str):
        somme += len(a)
    if isinstance(b, int):
        somme += b
    if isinstance(b, str):
        somme += len(b)
    return somme

print(additionner(5, "aaaa"))

# HERITAGE MULTIPLE : MULTIPLE-INHERITANCE

lion = Lion()
lion.afficher_infos()
lion.chasser_et_manger_proie()
