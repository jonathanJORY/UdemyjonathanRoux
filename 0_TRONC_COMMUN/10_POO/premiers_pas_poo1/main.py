class Personne:
    def __init__(self, nom: str="", age: int=0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.demander_nom()
        if age == 0:
            self.demander_age()

    def __str__(self):
        return self.nom + " agé de : "+str(self.age)+" ans."
    
    def afficher_infos(self):
        print(""+self.nom + " agé de : "+str(self.age)+" ans, je suis ") 
        if self.est_majeur():
            print("majeur" )
        else: 
            print("mineur")

    def demander_age(self):
        self.age = input(f"Bonjour {self.nom} quel est votre age ? ")

    def demander_nom(self):
        self.nom = input(f"Bonjour quel est votre nom ? ")

    def est_majeur(self):
        return self.age >=18


bob = Personne("bb",5)
bob.afficher_infos()
print(bob)