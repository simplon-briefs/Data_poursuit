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

    def retour_db(self, colonne, table):
        self.curseur.execute(f"SELECT {colonne} FROM {table}")
        infos = list(self.curseur.fetchall())
        return infos

    def retour_db_con(self, colonne, table, condition):
        self.curseur.execute(f"SELECT {colonne} FROM {table} WHERE {condition}")
        infos = list(self.curseur.fetchall())
        return infos


    def infos_questions(self):
        liste_finale = list()
        liste_theme = list()
        liste_questions = self.retour_db("libelle_question","questions")
        for numero in range(3):
            question_tuple = liste_questions[numero]
            question = str(*question_tuple)
            id_question = liste_questions.index(question_tuple) + 1
            reponse_v = str(*(self.retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 1")))[0])
            reponse_f = self.retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 2"))

            liste_finale.append(Question(id_question, question, reponse_v, reponse_f))
            liste_theme.append(*self.retour_db_con("difficulte_question", "questions", f"id_question = {id_question}")[0])
        return liste_finale, liste_theme


liste_finale, liste_theme = Connexion().infos_questions()

for instance in liste_finale:
    print(instance.display())