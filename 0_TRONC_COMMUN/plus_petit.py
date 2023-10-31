# LISTES - ALGO : VALEUR LA PLUS PETITE


nom_chauffeur =       ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5,      2.2,    0.4,    0.9,    7.1,     1.1,      0.6]

# méthode 1
distance_min = min(distance_chauffeur_km)
tuple_min = (nom_chauffeur[distance_chauffeur_km.index(distance_min)],distance_min)
print(tuple_min)

#méthode 2
i_min = 0
for i in range(len(distance_chauffeur_km)):
    if distance_chauffeur_km[i] < distance_chauffeur_km[i_min]:
        i_min = i
print(nom_chauffeur[i_min])