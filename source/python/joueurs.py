
class Joueur:

    def __init__(self, id, nom, couleur, score, camembert):
        self.id = id
        self.nom = nom
        self.couleur = couleur
        self.score = score
        self.camembert = camembert
        
    @classmethod
    def infos(cls, nb_joueurs):
        lst = []
        for i in range(nb_joueurs):
            nouveau = Joueur(id, input(f"pseudo joueur n°{i+1}: "), input("Choix de la couleur : "), 0 ,0)
            lst.append(nouveau)
        return lst