from requettes import Connection
from question import Question 
import random

def get_random_question(liste):
    random.shuffle(liste)
    return liste 

cnx = Connection()
liste = cnx.get_questions_reponse()
liste_random = get_random_question(liste)
print(liste_random)
