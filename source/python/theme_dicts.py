import requettes
from requettes import liste_finale, liste_theme

liste_titres = ["Big Data", "Thème 2", "Thème 3", "Thème 4", "Thème 5"]

def creer_dico_theme(index_theme):
    liste_dico = []
    dico_theme = dict()
    for numero in range(len(liste_finale)):
        if liste_theme[numero] == index_theme:
            liste_dico.append(liste_finale[numero])
    dico_theme[liste_titres[index_theme-1]] = liste_dico
    return dico_theme

dicte = creer_dico_theme(1)

print(dicte)
