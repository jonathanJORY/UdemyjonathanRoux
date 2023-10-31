# LES COLLECTIONS : LISTES / TUPLES
# Exercice "in insensible à la casse"


def element_dans_liste(e, l):
    '''for el in l:
        if e.lower() == el.lower():
            return True
    return False'''
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]











