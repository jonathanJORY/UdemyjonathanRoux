class Pizza:

    def __init__(self, nom: str, prix: float, ingredients: list, vegetarienne: bool=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne


    def __str__(self):
        return "La pizza: "+self.nom + " est au prix de: "+ str(self.prix) +" €\nLa liste des ingrédients: "+ ", ".join(self.ingredients) + " \n" + ("--VEGETARIENNE--\n" if self.vegetarienne else "--NON VEGETARIENNE--\n")
    
    #def afficher()


class PizzaPersonalise(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    index_pizza_perso = 0
    def __init__(self):
        PizzaPersonalise.index_pizza_perso += 1
        self.numero = PizzaPersonalise.index_pizza_perso
        super().__init__("", 0, [])
        self.nom = input("Choissisez un nom pour votre pizza: ") +  " "+str(self.numero)
        self.demander_ingredient()
        self.calculer_prix()

    def calculer_prix(self):
        self.prix = len(self.ingredients)*self.PRIX_PAR_INGREDIENT + self.PRIX_DE_BASE

    def demander_ingredient(self):
        print("\n---")
        ingredient = input(f"Ajouter un ingrédient à votre {self.nom} n° {self.numero}(ou taper sur ENTRER pour finir): ")
        if ingredient != "":
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s): {', '.join(self.ingredients)}")
            self.demander_ingredient()
        return

pizzas = [
    Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Hawai", 9.5, ("tomate", "ananas", "oignons")),
    Pizza("4 saisons", 11, ("oeuf", "emmental", "tomate", "jambon", "olives")),
    Pizza("Végétarienne", 7.8, ("champignons", "tomate", "oignons", "poivrons"), True),
    PizzaPersonalise(),
]

# Filtre

for pizza in pizzas:
    if pizza.prix<10 and "tomate" in pizza.ingredients and not pizza.vegetarienne:
        print(pizza)

# tri
def tri(e):
    return e.prix

pizzas.sort(key=tri)