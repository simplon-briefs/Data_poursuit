from joueurs import joueurs


rep1 = "la bonne"
def verif_rep(rep_utilisateur, vrai_reponse, lst):

    if rep_utilisateur == vrai_reponse:
        lst[0].score = lst[0].score + 1
        print(f"Bravo! Tu peux rejouer, Vos points : {lst[0].score}")
    else:
        print(f"Mauvaise réponse, votre score est : {lst[0].score}")
        
saisie_nbr_joueurs = int(input("Nombre de joueur : "))
lst_joueurs = joueurs.infos(saisie_nbr_joueurs)
saisie_choix = input("entrez votre choix : ")

# print(lst_joueurs[0].nom, lst_joueurs[0].couleur, lst_joueurs[0].score)
# # point = lst_joueurs[0].score
# # print(point)
verif_rep(saisie_choix, rep1, lst_joueurs)
# print(lst_joueurs[0].nom, lst_joueurs[0].couleur, lst_joueurs[0].score)
for joueur in lst_joueurs:
    print(joueur.nom, joueur.couleur, joueur.score)