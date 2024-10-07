
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
