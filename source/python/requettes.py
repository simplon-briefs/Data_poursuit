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
            # print(theme_fetchall)
            # print(ques_fals)
            # print(ques_true)
            # print(i)
            liste_instance_question.append(instance_question)
            dico_inctance_question[theme_fetchall] = liste_instance_question
        return dico_inctance_question
        # print("-------------")
        # print(dico_inctance_question["Big Data"][0].display())


    # def retour_db(self, colonne, table):
    #     self.curseur.execute(f"SELECT {colonne} FROM {table}")
    #     infos = list(self.curseur.fetchall())
    #     return infos

    # def retour_db_con(self, colonne, table, condition):
    #     self.curseur.execute(f"SELECT {colonne} FROM {table} WHERE {condition}")
    #     infos = list(self.curseur.fetchall())
    #     return infos


    # def infos_questions(self):
    #     liste_finale = list()
    #     liste_theme = list()
    #     liste_questions = self.retour_db("libelle_question","questions")
    #     for numero in range(3):
    #         question_tuple = liste_questions[numero]
    #         question = str(*question_tuple)
    #         id_question = liste_questions.index(question_tuple) + 1
    #         reponse_v = str(*(self.retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 1")))[0])
    #         reponse_f = self.retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 2"))

    #         liste_finale.append(Question(id_question, question, reponse_v, reponse_f))
    #         liste_theme.append(*self.retour_db_con("difficulte_question", "questions", f"id_question = {id_question}")[0])
    #     return liste_finale, liste_theme


#liste_finale, liste_theme = Connexion().infos_questions()
#Connexion().compute()
