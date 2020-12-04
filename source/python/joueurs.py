
class Joueur:

    def __init__(self, id, nom, couleur):
        self.id = id
        self.nom = nom
        self.couleur = couleur
        self.score = {}
        self.camembert = 0
        
    @classmethod
    def infos(cls, nb_joueurs):
        lst = []
        for i in range(nb_joueurs):
            nouveau = Joueur(id, input(f"pseudo joueur n°{i+1}: "), input("Choix de la couleur : "), {'Big Data' : 0, 'IA' : 0, 'math' : 0, 'ethique' : 0, 'pytohn' : 0} ,0)
            lst.append(nouveau)
        return lst