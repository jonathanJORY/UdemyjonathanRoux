"""module de base input print """
def est_majeur(age: int):
    """
    Si l'âge est supérieur ou égal à 18 ans, renvoie Vrai, sinon renvoie Faux.

    :param age: entier
    :type age: int
    :return: Vrai ou faux
    """
    if age <= 0:  # "40" <= 0
        return False
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero_personne):
    """
    Il demande à l'utilisateur un nom et un âge, et les renvoie sous forme de tuple

    :param numero_personne: Le numéro de la personne que nous demandons
    :return: le nom et l'âge de la personne.
    """
    nom_personne = input("Nom de la personne " + str(numero_personne) + ": ")
    age_personne = input("Age de la personne " + str(numero_personne) + ": ")
    return nom_personne, int(age_personne)


def afficher_infos_personne(numero_personne, nom, age: int):
    """
    Il imprime le nom et l'âge d'une personne, et si oui ou non ils sont un adulte

    :param numero_personne: un argument positionnel
    :param nom: un string
    :param age: int - Il s'agit d'un argument de mot-clé.
    Il indique à Python que le paramètre age doit
    être un entier
    :type age: int
    """
    print("La personne n°", numero_personne, " est: ", nom, " son age est: ", age, "ans")
    print("le nom possède ", len(nom), " caractères")
    if est_majeur(age):
        print("il est majeur")
    else:
        print("il est mineur")

def recuperer_et_afficher_infos_personne(numero_personne):
    """
    Il récupère et affiche les informations d'une personne

    :param numero_personne: le numéro de la personne
    """
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

NB_PERSONNES = 2

for i in range(NB_PERSONNES):  # 0 1 2
    recuperer_et_afficher_infos_personne(i+1)

afficher_infos_personne("007", "James", 40)
