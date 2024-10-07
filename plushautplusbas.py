from random import randint

def nombreAleatoire(maximum):
    """
    Génère un nombre aléatoire entre 1 et le maximum
    """
    return randint(1,maximum+1)

def entreeUtilisateur():
    """
    Demande d'entrer un chiffre sur la console et le renvoie.
    Renvoie un entier valide, ou raise une ValueError au delà de 10 tentatives
    """
    a = None
    c = 0
    while a == None:
        try:
            a = int(input("Entrez un chiffre: "))
        except ValueError:
            print("Le nombre entrée n'est pas un entier")
            c = c + 1
            if c == 10:
                print("Vous avez atteint le nombre limite d'erreurs")
                raise ValueError
    return a

def plushautplusbas(entree,reponse):
    """
    Compare le chiffre entrée avec celui qu'il faut deviner
    Si ils sont égaux, renvoyer 0
    Si l'entrée est plus petite, renvoyer 1
    Si l'entrée est plus grande, renvoyer -1
    """
    if entree < reponse:
        return 1
    elif entree > reponse:
        return -1
    else:
        return 0

nombre_a_deviner = nombreAleatoire(100)




comparaison = 2
while comparaison != 0:
    try:
        entree = entreeUtilisateur()
    except ValueError:
        print("Trop d'entrée incorrects, on s'arrète")
        print("La bonne réponse était "+str(nombre_a_deviner))
        exit()
    comparaison = plushautplusbas(entree,nombre_a_deviner)
    if comparaison > 0:
        print("Trop petit")
    if comparaison < 0:
        print("Trop grand")
    if comparaison == 0:
        print("Gagné")
