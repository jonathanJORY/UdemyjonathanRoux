"""utilisation module turtle et boucle"""

import turtle


def escalier(taille, nombre):
    """
    Il dessine un escalier de taille 'taille' et 'nombre' marches

    :param taille: la longueur du côté du carré
    :param nombre: nombre d'étapes
    """
    for _ in range(0, nombre):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def carre(taille):
    """
    Il dessine un carré d'une taille donnée

    :param taille: la longueur des côtés du carré
    """
    for _ in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nombre):
    """
    Il dessine des carrés de taille croissante

    :param taille_depart: la taille du premier carré
    :param nombre: le nombre de cases à dessiner
    """
    for i in range(0, nombre):
        taille = (i+1)*taille_depart
        carre(taille)


t = turtle.Turtle()

# escalier(30, 5)
# carre(50)
carres(2, 10)

turtle.done()
