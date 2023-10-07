"""Convertisseur d'unité"""
# unité de départ, unité d'arrivée, facteur de conversion
CONVERSIONS = (
    ("pouces", "cm", 2.54),
    ("m", "cm", 100),
    ("km", "miles", 0.621371),
    ("yard", "m", 0.9144),
    ("kg", "livres", 2.20462),
)


def demander_et_afficher_conversion(entrer1: str, entrer2: str, diviseur:
    float, inverse: bool = False):
    """
    Il demande à l'utilisateur un
    nombre, le convertit dans l'autre unité et imprime le résultat

    :param entrer1: Le nom de la première unité
    :type entrer1: str
    :param entrer2: Le nom de l'unité vers laquelle vous souhaitez effectuer la conversion
    :type entrer2: str
    :param diviseur: le nombre par lequel diviser pour passer d'une unité à l'autre
    :type diviseur: float
    :param inverse: booléen = Faux, defaults to False
    :type inverse: bool (optional)
    """
    if inverse:
        entrer1, entrer2 = entrer2, entrer1
        diviseur = 1 / diviseur

    valeur_str = input(f"""Conversion {entrer1} -> {entrer2}.
Donnez la valeur en {entrer1} (ou 'q' pour quitter) : """)
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(entrer1, entrer2, diviseur)

    valeur_convertie = round(valeur_float * diviseur, 2)
    print(f"""Résultat de la conversion :
{valeur_float} {entrer1} = {valeur_convertie} {entrer2}""")
    return False


def demander_valeur_numerique_utilisateur(valeur_max):
    """
    Il demande à l'utilisateur un nombre entre deux valeurs,
    et si l'utilisateur n'entre pas un nombre
    entre ces deux valeurs, il demande à nouveau

    :param valeur_min: La valeur minimale que l'utilisateur peut entrer
    :param valeur_max: La valeur maximale que l'utilisateur peut entrer
    :return: la valeur de v_int.
    """
    valeur_str= input(f"Donnez une valeur entre 1 et {valeur_max} : ")
    try:
        v_int = int(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_utilisateur(valeur_max)

    if not 1 <= v_int <= valeur_max:
        print(f"ERREUR : Votre valeur doit être entre 1 et {valeur_max}")
        return demander_valeur_numerique_utilisateur(valeur_max)

    return v_int


# Menu : choix de la conversion

def main():
    """
    Il affiche un menu d'options de conversion, demande à l'utilisateur d'en choisir une,
    puis demande à l'utilisateur une valeur à convertir
    """
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    i = 1
    for (premier, deuxieme, _) in CONVERSIONS:
        unit1 = premier
        unit2 = deuxieme
        print(f"{i} - {unit1} vers {unit2}")
        i += 1
        print(f"{i} - {unit2} vers {unit1}")
        i += 1
    print(f"{i} - Quitter")

    choix_int = demander_valeur_numerique_utilisateur(i)

    while True:
        if choix_int == i:
            break
        index = (choix_int-1)//2
        reverse = choix_int % 2 == 0
        unit1, unit2, facteur = CONVERSIONS[index]

        if demander_et_afficher_conversion(unit1, unit2, facteur, reverse):
            break
main()
