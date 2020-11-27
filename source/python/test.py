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
        dico[str(*liste_cles[i])] = str(*liste_valeurs[i])
    return dico


liste_questions = retour_db("libelle_question","questions")
liste_reponses = retour_db("libelle_reponse", "reponses")

dico_qr = creer_dico(liste_questions, liste_reponses)

for i in dico_qr:
    print(f"Question : {i}\nRéponse 1 : {dico_qr[i]}\nRéponse 2 : Réponse fausse")
    reponse_joueur = int(input("1 ou 2"))
    if reponse_joueur == 1:
        print("Correct !")