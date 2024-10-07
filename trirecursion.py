
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


def triNaifIteratif(tab):
    """
    Trie un tableau sur place à l'aide du tri naif : cherche le plus petit élément et le met en
    tête du tableau, puis le plus petit suivant, etc
    """
    # Pour chaque taille du tableau (on élimie à chaque itération le 1er élément)
    for i in range(0,len(tab)):
        # Trouver le plus petit élément
        min = tab[i]
        indexMin = i
        for c in range(i,len(tab)):
            if tab[c] < min:
                indexMin = c
                min = tab[c]
        

        # Ramener le plus petit élément en 1ere position
        # Swap l'élément i avec l'élément j
        tab[i],tab[indexMin] = tab[indexMin],tab[i]
        # (code équivalent à celui-ci :)
        # temp = tab[i]
        # tab[i] = tab[j]
        # tab[j] = temp


def triRapideRecursif(tab):
    """
    Renvoie un tableau trié
    Recursion :
        - Pivot : 1er élément du tableau
        - construit deux sous tableau :
            - tous les elts plus petits que le pivot
            - tous les elts plus grand ou égal que le pivot
        - 2 appels recursifs sur les deux sous tableaux
        - résultat : concaténation sousTableau1 + pivot + sousTableau2
    Condition limite : tableau de 1 element ou 0 élement est déjà trié
    """
    # Condition limite
    if len(tab) <= 1:
        return tab
    
    pivot = tab[0]
    sousTableau1 = []
    sousTableau2 = []
    for elt in tab[1:]:
        # Remplissage des deux sous tableau
        if elt < pivot:
            sousTableau1.append(elt)
        else:
            sousTableau2.append(elt)
    # Appels recursifs sur les deux sous tableaux
    sousTableau1 = triRapideRecursif(sousTableau1)
    sousTableau2 = triRapideRecursif(sousTableau2)

    # Reconstituer le tableau final
    return sousTableau1 + [pivot] + sousTableau2


tableauTest1 = [1,5,3,5,6,7,3,4,5]
tableauTest2 = [1,5,3,5,6,7,3,4,5]

triNaifIteratif(tableauTest1)
print(tableauTest1)

tableauTest2 = triRapideRecursif(tableauTest2)
print(tableauTest2)