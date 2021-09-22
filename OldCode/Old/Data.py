from faker import Faker

f = Faker(locale='zh_CN')

for i in range(0,28):
     print(f.name()+"X")
    # print(f.ssn())
    # print(f.email())
    # print(f.ssn(min_age=18, max_age=45, gender=None))

'''
去重算法
'''
a = ['a','b','b','c','c','d','e','e']
b = []
for i in a:
     if i in b:
          pass
     else:
          b.append(i)

print(b)

