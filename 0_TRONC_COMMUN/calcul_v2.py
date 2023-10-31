"""Utilisations de dictionnaires"""

def afficher_table(nombre, operateur_str):
    """
    La fonction `afficher_table` prend en entrée un nombre `nombre` et une chaîne d'opérateur
    `operateur_str`, et imprime le tableau des calculs en utilisant l'opérateur donné
    et les nombres de 1 à 9.

    :param nombre: Le paramètre `nombre` représente le nombre qui sera utilisé dans le table
    :param operateur_str: Le paramètre `operateur_str` est une chaîne qui représente l'opérateur à
    utiliser dans les calculs.
    :return: La fonction `afficher_table` renvoie `Aucun`.
    """
    operations = {
        "x": lambda a, b: a * b,
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "^": lambda a, b: a**b #pow(a, b)
    }

    operation_cbk = operations.get(operateur_str)

    if operation_cbk is None:
        print("Opérateur non pris en charge")
        return

    for i in range(1, 10):
        print(i, operateur_str, nombre, "=", operation_cbk(i, nombre))


# FONCTIONS LAMBDA

afficher_table(2, "x")
print()
afficher_table(2, "+")
print()
afficher_table(2, "g")
print()
afficher_table(2, "^")

def somme(titre, *nombres): #, **matieres):
    # *nombres = un tuple de taille 0,n
    # **matieres = un dictionnaires de taille 0,n
    """
    La fonction "somme" prend un titre et un nombre quelconque d'arguments,
    et renvoie la somme de tous les arguments.

    :param titre: Le paramètre "titre" est une chaîne.
    Il est utilisé pour fournir un titre descriptif pour le calcul de la somme
    :return: la somme de tous les nombres passés en arguments.
    """
    print("TITRE:", titre)
    resultat = 0
    for nombre in nombres:
        resultat += nombre
    return resultat

print(somme("somme des notes"))


def afficher_table_multiplication(nombre, mini=1, maxi=10):
    """
    Il imprime la table de multiplication d'un nombre n, entre mini et maxi

    :param nombre: le nombre à multiplier par
    :param mini: La valeur miniimale par laquelle multiplier, defaults to 1 (optional)
    :param maxi: La valeur maxiimale à afficher, defaults to 10 (optional)
    :return: la multiplication des deux nombres.
    """
    if mini > maxi:
        print("ERREUR : Le mini est supéreur au maxi")
        return

    for i in range(mini, maxi+1):
        print(i, "x", nombre, "=", i*nombre)


afficher_table_multiplication(5)
