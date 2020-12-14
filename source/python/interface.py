from tkinter import *
from requettes import Connexion
import random
from joueurs import Joueur

class Root:
    def __init__(self):
        self.root=Tk()
        self.root.title =("titre")
        self.root.geometry("900x1130")
        self.root.minsize(480, 360)
        self.root.config(background="white")

        self.values = [StringVar(), StringVar(), StringVar()]
        self.joueur = [StringVar(), StringVar()]
        self.joueur_liste = []


        self.question_reponse = Connexion().compute()
        self.compute()
        self.selected_player = 0

    
    def get_random_question(self, liste):
        random.shuffle(liste)
        return liste

    def compute(self):
        self.main()


    def main(self):
        Label(self.root, text="score").grid(row=6, column=1)
        Label(self.root, text="nom").grid(row=7, column=1)

        question_reponse_random = self.get_random_question(self.question_reponse)
        poiteur = random.randint(0, len(question_reponse_random))
        poiteur -=1
        liste_question_reponse = question_reponse_random
        Label(self.root, text=liste_question_reponse[poiteur].question,height=5).grid(column=2, row=1)

        if len(liste_question_reponse[poiteur].reponse_all) == 1:
            self.reponse_simple(liste_question_reponse[poiteur])
        else:
            self.reponse_multiple(liste_question_reponse[poiteur])
    
    def reponse_simple(self, liste_reponse):
        Label1 = Label(self.root, text = 'Reponse de question : ')
        Label1.grid(column=1, row=3, sticky='w')
        Champ = Entry(self.root, textvariable= self.values[0], width=31)
        Champ.focus_set()
        Champ.grid(column=2, row=3, sticky='sw', columnspan=2, padx=10)
        bouton2= Button (self.root, text="Envoyer", command=lambda: self.verif_rep(self.values[0], liste_reponse), pady=2)
        bouton2.grid(column=2, row=3,sticky='sw',pady=20)

    def reponse_multiple(self, liste_reponse):
        for i in range(len(liste_reponse.reponse_all)):
            self.values[i]= liste_reponse.reponse_all[i]
            Button(self.root, text=liste_reponse.reponse_all[i], command=lambda name=self.values[i]: self.verif_rep(name, liste_reponse)).grid(row=2, column=(i+1))
    
    def verif_rep(self, item, instance):
        print(instance.reponse_true)
        print(item)
        if item  == instance.reponse_true:
            self.reload_window()
        else:
            self.joueur_liste = self.tour_player()
            self.reload_window()

    def reload_window(self):
        label = Label(self.root, text="Bonne reponse").grid(column=2, row=3)
        liste = self.root.grid_slaves()
        for l in liste:
            l.destroy()
        self.main()

    
        

    def add_joueur(self, joueur):
        j = Joueur(1,joueur[0].get(), joueur[1].get())
        self.joueur_liste.append(j)
        print(self.joueur_liste[0].nom)

    def end_joueur(self):
        self.reload_window()

    def tour_player(self):
        if self.selected_player + 1 <= 1:
            self.selected_player + 1
            return self.selected_player
        else:
            self.selected_player = 0
            return self.selected_player

Root().root.mainloop()