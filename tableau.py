
def entreeTableau(a):
    """
    Cette fonction demande à l'utilisateur d'entrée une série de valeur numérique,
    elle les mets dans une liste, et renvoie la liste à la première valeur entrée
    qui n'est pas numérique.

    :return une liste de valeur numérique entrée par l'utilisateur
    """
    tab = []
    while True:
        try:
            n = int(input('Entrez une valeur numérique, ou "fin" pour finir: '))
            tab.append(n)
        except ValueError:
            break

    return tab


def factorielle(n):
    """
    Calcul de la factorielle de n de manière récursive
    Récursion : n! = n * (n-1)!
    Condition Limite : 1! = 1
    """
    # Commencer par la condition limite !
    if n == 1:
        return 1
    # Récursion
    else:
        return n * factorielle(n-1)


def sommeRecursive(tab):
    """
    Somme tous les chiffres de 1 à n dans un tableau.
    Récursion : si tab à une longueur n, on ajoute le dernier élément aux n-1 premiers éléments
    Condition de fin : si len(tab)==0, la somme est 0
    """
    # Condition limite
    if len(tab) == 0:
        return 0
    # Récursion (len(tab) > 0)
    # Ajoute le dernier élément à la somme des n-1 premiers éléments
    return tab[len(tab)-1] + sommeRecursive(tab[0:-1])
