from requettes import Connection
from question import Question 
from joueurs import Joueur
import random

def get_random_question(liste):
    random.shuffle(liste)
    return liste 

def verif_rep(rep_utilisateur, vrai_reponse, lst):

    if rep_utilisateur == vrai_reponse:
        lst[0].score = lst[0].score + 1
        print(f"Bravo! Tu peux rejouer, Vos points : {lst[0].score}")
        return True
    else:
        print(f"Mauvaise réponse, votre score est : {lst[0].score}")
        return False

def main():
    cnx = Connection()
    liste = cnx.get_questions_reponse()
    liste_random = get_random_question(liste)
    print(liste_random)

    lst_joueurs = Joueur.infos(int(input("Nombre de joueur : ")))

    
    for joueur in lst_joueurs:
        tmp = True
        liste_random = get_random_question(liste)
        i = 0
        print(f"Nom : {joueur.nom}\n couleur : {joueur.couleur}\n score : {joueur.score}\n camembert : {joueur.camembert}")
        while tmp :             
            print(liste_random[0].question)
            print(liste_random[0].reponse_all)
            print(liste_random[0].reponse_true)
            saisie_choix = input("entrez votre choix : ")
            #verif_rep(saisie_choix, question.reponse_true, lst_joueurs)
            i += 1
            #saisie_choix == liste_random[0].reponse_true
            if True :
                joueur.score = joueur.score + 1
                print(f"Bravo! Tu peux rejouer, Vos points : {joueur.score}")
            else:
                print(f"Mauvaise réponse, votre score est : {joueur.score}")
                break
                


main()