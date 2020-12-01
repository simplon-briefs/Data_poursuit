from requettes import Connexion
from question import Question 
from joueurs import Joueur
import random


def get_random_question(liste):
    random.shuffle(liste)
    return liste 


def jeu(lst, lst2):
    tour = True
    while tour :
        for joueur in lst:
            tmp = True
            print(f"Nom : {joueur.nom}\n couleur : {joueur.couleur}\n score : {joueur.score}\n camembert : {joueur.camembert}")
            print(lst2.keys())
            saisie_theme = input("choisisez le theme : ")
            liste_inter = lst2[saisie_theme]
            liste_random = get_random_question(liste_inter)
            i = 0
            while tmp :  
                print(liste_random[i].question)
                print(liste_random[i].reponse_all)
                vrais = liste_random[i].reponse_true
                saisie_choix = input("entrez votre choix : ")
                i += 1
                if saisie_choix.lower() == vrais.lower() : # verif question  
                    joueur.score[saisie_theme] = joueur.score[saisie_theme] + 1
                    print(f"Bravo! Tu peux rejouer, Vos points en {saisie_theme} : {joueur.score[saisie_theme]}")
                    if joueur.score[saisie_theme] == 5 :
                        joueur.camembert = joueur.cammembert + 1
                        if joueur.camembert == 1 :
                            return
                else:
                    print(f"Mauvaise réponse, votre score actielle en {saisie_theme} : {joueur.score[saisie_theme]}")
                    tmp = False 
                


def main():
    cnx = Connexion()
    liste_question = cnx.compute()
    lst_joueurs = Joueur.infos(int(input("Nombre de joueur : ")))
    jeu(lst_joueurs, liste_question)

    for joueur in lst_joueurs :
        print(f'Nom : {joueur.nom}\n Couleur : {joueur.couleur}\n Score : {joueur.score}\n Camembert : {joueur.camembert}')


main()