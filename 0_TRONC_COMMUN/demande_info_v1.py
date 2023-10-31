"""Module print input concaténation"""

def afficher_informations_personne(nom, age, taille=0):
    """
    Il prend un nom, un âge et une taille, et imprime un message basé sur l'âge

    :param nom: Ceci est un paramètre obligatoire
    :param age: Ceci est un paramètre obligatoire
    :param taille: C'est le paramètre par défaut.
    Si aucune valeur n'est passée pour ce paramètre, il
    prendra la valeur par défaut, defaults to 0 (optional)
    """
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

    print("L'an prochain vous aurez " + str(age + 1) + " ans")

    if age == 17:
        print("Vous êtres presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age in (1, 2):
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher la taille
    if taille != 0:
        print("Votre taille : " + str(taille) + " m")


def demander_nom():
    """
    Il demande à l'utilisateur son nom et le renvoie
    :return: la valeur de la variable response_nom.
    """
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    """
    Il demande à l'utilisateur son âge et le renvoie sous la forme d'un entier

    :param nom_personne: C'est le nom de la personne dont vous voulez connaître l'âge
    :return: L'âge de la personne
    """
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int

def demander_taille(nom):
    """
    Il demande à l'utilisateur un numéro, et si l'utilisateur entre un numéro, il renvoie ce numéro.
    Si l'utilisateur entre quelque chose qui n'est pas un nombre,
    il imprime un message d'erreur et demande
    à nouveau

    :param nom: Le nom de la personne
    :return: la valeur de la variable taille.
    """
    taille = 0
    while taille == 0:
        taille_str = input(nom + " quel est votre taille ?(1.84) ")
        try:
            taille = float(taille_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour la taille")
    return taille


NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    print("Personne n°",i)
    nom_entrer = demander_nom()
    age_entrer = demander_age(nom_entrer)
    taille_entrer = demander_taille(nom_entrer)
    afficher_informations_personne(nom_entrer, age_entrer, taille_entrer)
