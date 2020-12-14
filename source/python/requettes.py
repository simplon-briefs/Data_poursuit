import mysql.connector as mysql
from question import Question

class Connexion:
    def __init__(self):
        self.lien = mysql.connect(
            host='localhost',
            password='root',
            user='root',
            database='trivial'
            )
        self.curseur = self.lien.cursor()

    def compute(self): # la fonction recuper toute les info de la table questions
        dico_inctance_question = {}
        liste_instance_question = []
        self.curseur.execute("""SELECT id_question, libelle_question, id_theme FROM questions""")
        question_fetchall = self.curseur.fetchall()
        for i in question_fetchall:
            ques_true = None
            ques_fals = []
            self.curseur.execute("""SELECT libelle_reponse, valeur_reponse FROM reponses WHERE id_question = %d"""%(i[0]))
            reponse_fetchall = self.curseur.fetchall()
            self.curseur.execute("""SELECT nom_theme FROM theme WHERE id_theme = %d"""%(i[2]))
            theme_fetchall = self.curseur.fetchall()[0][0]
            for j in reponse_fetchall:
                if j[1] == 0:
                    ques_fals.append(j[0])
                elif j[1] == 1:
                    ques_true = j[0]
                else:
                    pass
            instance_question = Question(i[0], i[1], ques_true, ques_fals)
            liste_instance_question.append(instance_question)
            dico_inctance_question[theme_fetchall] = liste_instance_question
        return liste_instance_question
