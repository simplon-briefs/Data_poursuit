import mysql.connector as mysql

class Connection:
    def __init__(self):
        self.lien = mysql.connect(
            host='localhost',
            password='root',
            user='root',
            database='trivial'
            )
        self.curseur = self.lien.cursor()
cnx = Connection()

def retour_db(colonne, table):
    cnx.curseur.execute(f"SELECT {colonne} FROM {table}")
    infos = list(cnx.curseur.fetchall())
    return infos

def retour_db_con(colonne, table, condition):
    cnx.curseur.execute(f"SELECT {colonne} FROM {table} WHERE {condition}")
    infos = list(cnx.curseur.fetchall())
    return infos

def creer_dico(liste_cles, liste_valeurs):
    dico = {}
    for i in range(len(liste_cles)):
        dico[str(*liste_cles[i])] = str(liste_valeurs[i])
    return dico


liste_questions = retour_db("libelle_question","questions")
liste_reponses = retour_db("libelle_reponse", "reponses")

dico_qr = creer_dico(liste_questions, liste_reponses)

#for i in dico_qr:
    #print(f"Question : {i}\nRéponse 1 : {dico_qr[i]}\nRéponse 2 : Réponse fausse")
    #reponse_joueur = int(input("1 ou 2"))
    #if reponse_joueur == 1:
        #print("Correct !")

question = liste_questions[int(input("n° question ?")) - 1]
print(*question)
id_question = liste_questions.index(question) + 1
reponse_v = (retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 1")))[0]
reponse_f = retour_db_con("libelle_reponse", "reponses", str(f"id_question = {id_question} AND valeur_reponse = 2"))
print(*reponse_v)
print(reponse_f)