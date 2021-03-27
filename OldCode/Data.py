from faker import Faker

f = Faker(locale='zh_CN')

for i in range(0,28):
     print(f.name()+"X")
    # print(f.ssn())
    # print(f.email())
    # print(f.ssn(min_age=18, max_age=45, gender=None))
