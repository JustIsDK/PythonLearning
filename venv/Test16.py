class AnoySurvey():

    def __init__(self,question):
        self.question = question
        self.respon = []

    def show_question(self):
        print(self.question)

    def store_respon(self,new_respon):
        self.respon.append(new_respon)

    def show_result(self):
        print("Survey result: ")
        for respon in self.respon:
            print('- '+ respon)