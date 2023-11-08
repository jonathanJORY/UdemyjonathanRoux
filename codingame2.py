print(f"{sum((-1) ** i / (2 * i + 1) for i in range(int(input()))) * 4:.5f}")

# ou

n = int(input())

approximation = 0
sign = 1

for i in range(1, 2 * n, 2):
    approximation += sign * (1 / i)
    sign *= -1


pi_approximation = 4 * approximation

print(f"{pi_approximation:.5f}")

"""
calcul de l'approximation de Pi en utilisant la série de Madhava-Leibniz pour les premiers n termes. 
Le résultat est ensuite arrondi à cinq décimales après la virgule avant d'être imprimé.
"""

print(sum(int(input()) for _ in range(int(input()))) ** 2)

"""prend en entrée les entiers, calcule la somme des nombres donnés, trouve le carré de cette somme, puis imprime le résultat."""

# Lecture des entiers A et B
A = int(input())
B = int(input())

# Calcul du nombre de suppositions nécessaires
# La stratégie optimale consiste à diviser l'intervalle en deux à chaque supposition
# Ainsi, le nombre maximum de suppositions est le logarithme en base 2 de la longueur de l'intervalle, arrondi à l'entier supérieur
maximum_guesses = (B - A).bit_length()

# Affichage du nombre maximum de suppositions
print(maximum_guesses)

"""Ce code prend en entrée les entiers A et B, 
puis utilise la stratégie optimale pour calculer le nombre maximum de suppositions 
nécessaires pour deviner le nombre caché. La fonction bit_length() est utilisée pour calculer 
le logarithme en base 2 de la longueur de l intervalle. Le code affiche ensuite ce nombre maximum de suppositions."""

w,h=[int(i) for i in input().split()]
print(w if w==h else min(w,h)+1)

"""Ce code prend en entrée deux entiers, w et h, si w et h sont égaux, il imprime simplement w.
Sinon, il imprime le plus petit des deux nombres, plus un"""

print(1000-(int(input())*2))

"""JCP"""

print(int(input())*int(input())//60)
"""
calculer la quantité de sucre consommée par Johny en grammes, étant donné le temps pendant lequel 
il a mangé du sucre en secondes et la vitesse à laquelle il a mangé le sucre en grammes par minute

quantité de sucre = (temps en secondes * vitesse en grammes par minute) / 60
La vitesse est donnée en grammes/minute, le temps est en secondes, convertir le temps en minutes en le divisant par 60.
"""
