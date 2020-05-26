# import json

# num = [1,2,3,4,5,45,34,332,656,89]
#
# fil = 'E:\我的坚果云\文件\私人\Python\Testtxt\json.json'

# with open(fil,'w') as fil_ob:
#     json.dump(num,fil_ob)

# with open(fil)as fi_ob:
#     number = json.load(fi_ob)
# print(number)

# try:
#     with open(fil)as file:
#         username = json.load(file)
#         print('Welcome ' + username)
# except FileNotFoundError:
#     username = input('Please input your name: ')
#     with open(fil,'w') as file:
#         json.dump(username,file)
# #         print("We'll check your name, " + username + ' ~~')
# file = 'E:\我的坚果云\文件\私人\Python\Testtxt\Fav.json'
# # while True:
#     fav = input('Please input your favourrite number: ')
#
#     with open(file,'a') as fi_ob:
#         json.dump(fav,fi_ob)
#         print('OK,it has check')
# with open(file)as fil_obj:
#     fav = json.load(fil_obj)
#     print('This is your fav number: '+ fav + ' !')

def get_full_name(first,middle,last):
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
