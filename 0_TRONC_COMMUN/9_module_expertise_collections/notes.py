# ---- COLLECTIONS : LISTES / TUPLES ----

noms = ["Jean", "Sophie", "Martin"]
noms_supplementaires = ["Christophe", "Zoe"]

# ---- AJOUTER DES ÉLÉMENTS ----

# Utilisation de append pour ajouter un élément à la liste
noms.append("Toto")

# Utilisation de insert pour ajouter un élément à une position spécifique
noms.insert(1, "Toto")

# Utilisation de append pour ajouter une liste en tant qu'élément
noms.append(noms_supplementaires)  # ["Jean", "Sophie", "Martin", ["Christophe", "Zoe"]]

# Utilisation de extend (ou +=) pour ajouter tous les éléments d'une autre liste
noms.extend(noms_supplementaires)

# ---- SLICING ----

# Créer une copie superficielle de la liste
slices_noms = noms[:]
# ou
slices_noms = noms.copy()

# ---- TRIER UNE LISTE ----

# Trier une liste selon une fonction clé
def tri_longeur_caracteres(nom):
    return len(nom)

# Tri en place
noms.sort(key=tri_longeur_caracteres, reverse=True)

# Tri pour obtenir une nouvelle liste
noms_tries = sorted(noms, key=tri_longeur_caracteres, reverse=True)

# ---- ÉCHANGER DEUX ÉLÉMENTS (SWAP) ----

noms[0], noms[4] = noms[4], noms[0]

# ---- JOIN ET SPLIT ----

# Convertir une liste en une chaîne de caractères
noms = ["Jean", "Sophie", "Martin"]
noms_join = ", ".join(noms)

print("Nombre total de caractères:", len("".join(noms)))

# Convertir une chaîne de caractères en liste
noms_reconstruits = noms_join.split(", ")

# ---- COMPRÉHENSIONS DE LISTES ----

# Créer une nouvelle liste basée sur une condition
longeur_noms = [len(nom) for nom in noms if len(nom) < 10]

# Créer une nouvelle liste avec des valeurs conditionnelles
longeur_noms_condition = [1 if len(nom) < 10 else 0 for nom in noms]

# ---- AFFICHAGE DES RÉSULTATS ----

print(noms)
print(noms_tries)
print(noms_join)
print(noms_reconstruits)
print(longeur_noms)
print(longeur_noms_condition)
