import random 


class Question:
    def __init__(self, id_question, question, reponse_true, reponse_fake):
        self.id_question = id_question
        self.question = question
        self.reponse_true = reponse_true
        self.reponse_fake = [reponse_fake]

        self.reponse_all = reponse_fake[:]
        self.reponse_all.append(reponse_true)
 
    def display(self):
        print("id_question = ",self.id_question)
        print("reponse = ", self.question)
        print("reponse_true = ",self.reponse_true)
        print("reponse_fake = ", self.reponse_fake)
        print("reponse_all = ",self.reponse_all)
    
    def get_random_id_question(self):
        id_random = []
        for _ in range(10):
            id_random.append(random.randint(0,100))
        return id_random