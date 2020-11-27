
class joueurs:

    def __init__(self, id, nom, score, couleur):
        self.id = id
        self.nom = nom
        self.score = score
        self.couleur = couleur

    @classmethod
    def infos(cls, nb_joueurs):
        lst = []
        for i in range(nb_joueurs):
            nouveau = joueurs(id, input(f"pseudo joueur n°{i+1}: "), 0, input("Choix de la couleur : "))
            lst.append(nouveau)
        return lst

    # def score(self, rep):
    #     self.score = self.score + rep


print("hello world")
