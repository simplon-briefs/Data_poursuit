
class Joueur:

    def __init__(self, id, nom, score, couleur, camembert):
        self.id = id
        self.nom = nom
        self.score = score
        self.couleur = couleur
        self.camembert = camembert

    @classmethod
    def infos(cls, nb_joueurs):
        lst = []
        for i in range(nb_joueurs):
            nouveau = Joueur(id, input(f"pseudo joueur n°{i+1}: "), 0, input("Choix de la couleur : "),0)
            lst.append(nouveau)
        return lst