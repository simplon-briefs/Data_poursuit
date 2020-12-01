import random 


class Question:
    def __init__(self, id_question, question, reponse_true, reponse_fake):
        self.id_question = id_question
        self.question = question
        self.reponse_true = reponse_true
        self.reponse_fake = reponse_fake

        self.reponse_all = list(reponse_fake)
        self.reponse_all.append(reponse_true)
 
    def display(self):
        print("id_question = ",self.id_question)
        print("question = ", self.question)
        print("reponse_true = ",self.reponse_true)
        print("reponse_fake = ", self.reponse_fake)
        print("reponse_all = ",self.reponse_all)
    
    @classmethod
    def get_random_question(cls, liste):
        return random.shuffle(liste)