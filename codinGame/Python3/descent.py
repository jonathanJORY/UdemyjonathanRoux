import sys
import math

# game loop
while True:
    max_height = -1
    ind = -1
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > max_height:  # vérifier si la hauteur actuelle est supérieure à la hauteur maximale
            max_height = mountain_h  # mettre à jour la hauteur maximale si nécessaire
            ind = i # recuperer l'indice du max

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(ind)  # imprimer l'indice de la hauteur maximale
