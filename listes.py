fruits = ["banane","pomme","poire"]

# Boucler sur la liste
for fruit in fruits:
    print(fruit)

# Ajouter un raisin
fruits.append("raisin")
print(fruits)
# fruits devient ['banane', 'pomme', 'poire', 'raisin']
# Accès à la liste
print(fruits[1]) # pomme
print(fruits[0]) # banane
print(fruits[-1]) # raisin
print(fruits[-2]) # poire

fruits.append("ananas")
fruits.append("pasteque")
print(fruits)

# longueur d'une liste
print( len(fruits) ) # Affiche la longueur de la liste

#['banane', 'pomme', 'poire', 'raisin', 'ananas', 'pasteque']
#   0          1       2         3          4          5
# Slice
print(fruits[1:4]) # ['pomme', 'poire', 'raisin']
print(fruits[0:5]) # ['banane', 'pomme', 'poire', 'raisin', 'ananas']
print(fruits[:5]) # équivalent à fruits[0:5]
print(fruits[1:]) # implicitement il va jusqu'au bout ['pomme', 'poire', 'raisin', 'ananas', 'pasteque']
print(fruits[1:len(fruits)])

print(fruits[1:-1]) # ['pomme', 'poire', 'raisin', 'ananas']
print(fruits[1:-2]) # ['pomme', 'poire', 'raisin']
print(fruits[2:-5]) # []

liste = [0,1,2,3,4,5,6,7,8,9]
print(liste[0:6:2]) # [0, 2, 4]
print(liste[0:6:-1]) # []
print(liste[6:0:-1]) # [6, 5, 4, 3, 2, 1]

# Supprimer un élément de la liste
a = liste.remove(2)
print(liste) # [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(a)

# Le pop renvoie l'élément supprimé
liste = [0,1,2,3,4,5,6,7,8,9]
a = liste.pop(2)
print(liste) # [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(a)

# push/pop sert à simuler des piles


print()
print("==================")
print("=      PILE      =")
print("==================")
# lifo Last In First Out => pile
pile = []
# Empile deux éléments
pile.append("assiette1")
pile.append("assiette2")
pile.append("assiette3")
print("Pile : ",pile)

assiette = pile.pop()
print("Assiette prise : "+assiette)
print("Il reste sur la pile ",pile)

print()
print("==================")
print("=      FILE      =")
print("==================")
# fifo First In First Out => files
file = []
# Emfile deux éléments
file.append("client1")
file.append("client2")
file.append("client3")
print("File : ",file)

assiette = file.pop(0)
print("Client servi : "+assiette)
print("Il reste sur dans la file ",file)



print()
print("==================")
print("=   Boucles for  =")
print("==================")

print("Boucle sur tableau")
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

print("Boucle range(0,10)")
for i in range(0,10):
    print(i)


print("Boucle range(0,10,2)")
for i in range(0,10,2):
    print(i)
