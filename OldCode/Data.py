from faker import Faker

f = Faker(locale='zh_CN')

for i in range(0,7):
     print(f.name()+"静")
#     # print(f.ssn())
#     # print(f.email())
#     # print(f.ssn(min_age=18, max_age=45, gender=None))
#
#
# for i in range(0,5):
#      print('肥宅！！')