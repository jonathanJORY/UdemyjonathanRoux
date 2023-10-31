"""LES COLLECTIONS : LISTES / TUPLES Exercice in insensible à la casse"""


def element_dans_liste(e, l):
    """
    La fonction vérifie si un élément est présent dans une liste, en ignorant
    le respect de la casse.

    :param e: Le paramètre `e` représente l'élément dont on veut vérifier s'il est présent
    dans la liste `l`
    :param l: Une liste d’éléments à parcourir
    :return: une valeur booléenne indiquant si l'élément `e` est présent dans la liste `l`.
    
    for el in l:
        if e.lower() == el.lower():
            return True
    return False"""

    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]
