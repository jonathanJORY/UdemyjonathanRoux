"""Fichier de notes diverses"""
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
b = noms.extend(noms_supplementaires)
# print(b) = None

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


pizzas_nom = ("4 fromages", "Calzone", "Hawai")
pizzas_prix = (5.6, 5.7, 4.5)

# ---- ZIP ET UNZIP ----

# Utilisation de la fonction zip pour regrouper les tuples
objet_zip = zip(pizzas_nom, pizzas_prix)
list_zip = list(objet_zip)
print("Liste zip :", list_zip)

# Utilisation de la fonction zip pour décompresser les tuples
objet_unzip = zip(*list_zip)
list_unzip = list(objet_unzip)
print("Liste décompressée :", list_unzip)

#Supprimmer les doublons:
test = ['bob', 'pol','bob','lola']
test = list(set(test))


import time
res = 5
for i in range(res):
    time.sleep(1)
    print(".", end="", flush=True)
print()
# renvoie: ...........


for i in range(res):
    time.sleep(1)
    print(i, end="\r")
print()
# fait un chrono de 0 à i


print("bib",res,"n") # renvoie: bib 5 n
#print("bib"+res+"n")  renvoie: une erreur

print("-"*20) #  renvoie ----------------


a = print("tot")
print(a)
# renvoie tot puis None


a = 5

def ma_fonction():
    global a
    a = a + 1
    print(a)

ma_fonction()
ma_fonction()
# renvoie 6 puis 7


# inverser une chaine de caractere:
nom = "Jean"
print(nom[::-1])

# ou

r = ""
for c in nom:
    r = c + r

print(r)
#renvoie naeJ
