from faker import Faker

f = Faker(locale='zh_CN')

for i in range(0,10000):
    # print(f.name())
    # print(f.ssn())
    # print(f.email())
    print(f.phone_number())

