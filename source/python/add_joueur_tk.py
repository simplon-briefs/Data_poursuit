from tkinter import *
from requettes import Connexion
from joueurs import Joueur
from interface import Root

class Add_player:
    def __init__(self):
        self.root=Tk()
        self.root.title =("titre")
        self.root.geometry("900x1130")
        self.root.minsize(480, 360)
        self.root.config(background="white")

        self.name_player = StringVar()
        self.color_player = StringVar()
        self.widget()

    def widget(self):
        self.window_add_joueur()

    def window_add_joueur(self):
        Label(self.root, text = 'Nom : ').grid(column=2, row=1, sticky='w')
        Champ_name = Entry(self.root, textvariable= self.name_player, width=31)
        Champ_name.focus_set()
        Champ_name.grid(column=3, row=1, sticky='sw', columnspan=2, padx=10)

        Label(self.root, text = 'Couleur : ').grid(column=2, row=2, sticky='w')
        Champ_color = Entry(self.root, textvariable= self.color_player, width=31)
        Champ_color.focus_set()
        Champ_color.grid(column=3, row=2, sticky='sw', columnspan=2, padx=10)


        Button (self.root, text="Ajouter", command=lambda: self.add_joueur(self.name_player, self.color_player), pady=2).grid(column=2, row=11,sticky='sw',pady=20)
        Button (self.root, text="Fin", command=lambda: self.end_joueur(), pady=2).grid(column=3, row=11,sticky='sw',pady=20)

    def add_joueur(self, name_player, color_player):
        instance_joueur = Joueur(1, name_player, color_player)
        print(instance_joueur)
        self.name_player = ""
        self.color_player = ""
        self.widget()

    def end_joueur(self):
        self.reload_window()

    def reload_window(self):
        label = Label(self.root, text="Bonne reponse").grid(column=2, row=3)
        liste = self.root.grid_slaves()
        for l in liste:
            l.destroy()
        Root().compute()

Add_player().root.mainloop()