from Test16 import AnoySurvey

question = 'What language did you first learn to speak ?'
my_survey = AnoySurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    respon = input("Language: ")
    if respon == 'q':
        break
    if respon != ' ' or '':
        my_survey.store_respon(respon)

print("\nThank you to everyone who practised in the survey! ")
my_survey.show_result()

# from Test16 import AnoySurvey
#
# class TestAnoyServey(unittest.TestCase):
#     #
#     # def test_store_single_respon(self):
#     #     question = '你用的什么语言?'
#     #     my_servey = AnoySurvey(question)
#     #     my_servey.store_respon('English')
#     #
#     #     self.assertIn('English',my_servey.respon)
#     #
#     # def test_store_three_respon(self):
#     #     question = '你用的什么语言?'
#     #     my_servey = AnoySurvey(question)
#     #     respon = ['English','cc','aa']
#     #     for respons in respon:
#     #         my_servey.store_respon(respons)
#     #
#     #     for respons in respon:
#     #         self.assertIn(respons,my_servey.respon)
#
#     def setUp(self):
#         question = '你用的什么语言?'
#         self.my_survey = AnoySurvey(question)
#         self.respon = ['English','cc','aa']
#
#     def test_single_respon(self):
#         self.my_survey.store_respon(self.respon[0])
#         self.assertIn(self.respon[0],self.my_survey.respon)
#
# unittest.main()


‘’‘用来测试gitee功能’‘’