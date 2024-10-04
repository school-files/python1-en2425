import math
# from math import *
# from math import pi

def perimetreCercle(r):
    """
    Cette fonction calcule le périmètre d'un cercle.
    Le paramètre r correspond au rayon, et elle renvoie
    le périmètre dans la même unité que le rayon.
    """
    print("Pi: "+str(math.pi))
    return 2 * math.pi * r

def longueurPisteCourse(r,l):
    return perimetreCercle(r) + 2*l

def vitesse(temps, distance):
    """
    prend en paramètre un temps (en secondes) et une durée (en m)
    et qui renvoie la vitesse de course, en km/h
    """
    return distance / temps * 3.6

def vitessePiste(r,l,temps):
    return vitesse(temps,longueurPisteCourse(r,l))

r = int(input("Rayon de la piste ? "))
l = int(input("Longueur de la piste ? "))


## C'est moche, on va le mettre dans une boucle
# t1 = int(input("Temps du coureur 1 ? "))
# t2 = int(input("Temps du coureur 2 ? "))
# t3 = int(input("Temps du coureur 3 ? "))
# t4 = int(input("Temps du coureur 4 ? "))
# t5 = int(input("Temps du coureur 5 ? "))

# vitesseMoyenne = (vitessePiste(r,l,t1)+ \
#                  vitessePiste(r,l,t2)+ \
#                  vitessePiste(r,l,t3)+ \
#                  vitessePiste(r,l,t4)+ \
#                  vitessePiste(r,l,t5)) / 5
# print("La longueur de la piste est de "+str(longueurPisteCourse(r,l)))
# print("Temps du joueur 1 "+ str(t1))
# print("Temps du joueur 2 "+ str(t2))
# print("Temps du joueur 3 "+ str(t3))
# print("Temps du joueur 4 "+ str(t4))
# print("Temps du joueur 5 "+ str(t5))

# print("La vitesse moyenne est de "+str(vitesseMoyenne))

# Liste qui va contenir la vitesse de tous les coureurs
vitesseCoureurs = []

# Dans une boucle, demander 5 fois la vitesse d'un coureur et le mettre dans la liste


# Calculer la vitesse moyenne à partir de la liste
