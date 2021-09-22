users = {
    "name": 100,
    "age": 20,
    "helloworld":40,
    "xiaoming":42
}
# print(list(users.items()))

userlist = list(users.items())

userlist.sort(key=lambda x:x[1])
print(userlist)
# print(userlist[-1])
