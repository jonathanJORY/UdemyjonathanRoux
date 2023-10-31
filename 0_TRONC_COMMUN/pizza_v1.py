"""Utilisation de listes pour gérer des collections de pizzas"""
# def tri_personnalise(e):
#    return len(e)


def afficher(collection, n_premiers_elements=-1):
    """
    La fonction `afficher` prend une collection de pizzas et éventuellement un certain nombre de
    premiers éléments à afficher, trie la collection et imprime la liste des pizzas avec
    la première et la dernière pizza.

    :param collection: Le paramètre "collection" est une liste de noms de pizzas. Il représente la
    collection de pizzas que nous souhaitons exposer
    :param n_premiers_elements: Le paramètre `n_premiers_elements` est un paramètre facultatif qui
    spécifie le nombre d'éléments de la `collection` qui doivent être affichés. Par défaut, il est
    défini sur -1, ce qui signifie que tous les éléments de la « collection » seront affichés
    :return: La fonction ne renvoie explicitement rien. Cependant, il imprime la liste des pizzas et
    quelques informations complémentaires.
    """
    # collection.sort(key=tri_personnalise)
    pizza_liste = collection
    if n_premiers_elements != -1:
        pizza_liste = collection[:n_premiers_elements]
    nb_pizzas = len(pizza_liste)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return
    pizza_liste.sort()
    print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
    for i in pizza_liste:
        print(i)
    print()
    print("Première pizza: " + pizza_liste[0])
    print("Dernière pizza: " + pizza_liste[-1])


def ajouter_pizza_utilisateur(collection):
    """
    La fonction "ajouter_pizza_utilisateur" permet à l'utilisateur d'ajouter une pizza
    à une collection, en vérifiant si elle existe déjà avant de l'ajouter.

    :param collection: Le paramètre "collection" est une liste qui contient les pizzas existantes
    """
    entre_pizza = input("Pizza à ajouter: ")
    if entre_pizza.lower() in collection:
        print("ERREUR : Cette pizza existe déjà")
    else:
        collection.append(entre_pizza)




pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]

ajouter_pizza_utilisateur(pizzas)

afficher(pizzas, 2)
