from requettes import Connection
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
            liste_random = get_random_question(lst2)
            i = 0
            print(f"Nom : {joueur.nom}\n couleur : {joueur.couleur}\n score : {joueur.score}\n camembert : {joueur.camembert}")
            while tmp :    
                print(liste_random[i].question)
                print(liste_random[i].reponse_all)
                saisie_choix = input("entrez votre choix : ")
                i += 1
                print(i)
                if saisie_choix == 'bonne' : # verif question
                    joueur.score = joueur.score + 1
                    #joueur.camembert = 5
                    if joueur.score == 15 : 
                        return
                    print(f"Bravo! Tu peux rejouer, Vos points : {joueur.score}")
                else:
                    print(f"Mauvaise réponse, votre score actielle est : {joueur.score}")
                    tmp = False 

def main():
    cnx = Connection()
    liste = cnx.get_questions_reponse()
    lst_joueurs = Joueur.infos(int(input("Nombre de joueur : ")))
    jeu(lst_joueurs, liste)
    for joueur in lst_joueurs :
        print(f'Nom : {joueur.nom}\n Couleur : {joueur.couleur}\n Score : {joueur.score}\n Camembert : {joueur.camembert}')


main()