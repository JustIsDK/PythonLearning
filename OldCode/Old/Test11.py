# PI = 'E:\我的坚果云\文件\私人\Python\Testtxt\PI.txt'
# # with open('E:\Download\PI.txt')as file_object:
# #     contents = file_object.read()
# #     print(contents.rstrip())
# # with open(PI)as file_object:
# #     for line in file_object:
# #         print(line.rstrip())
#
# with open(PI) as file_object:
#     lines = file_object.readlines()
# PI_string = ''
# for line in lines:
#     PI_string += line.strip()
# # print(PI_string)
# # print(len(PI_string))
# birthday = input('Please input your birthday date: ')
# if birthday in PI_string:
#     print('Your birthday in PI !')
# else:
#     print('Sorry~~')
#
# #
# PTXT = 'E:\我的坚果云\文件\私人\Python\Testtxt\Python_learn.txt'
# with open(PTXT) as file_object:
#     PY = file_object.read()
#     PY.replace('Python','C++')
#     print(PY)

# with open(PTXT,'a') as file_object:
#     file_object.write('第一次尝试写入文件第四行\n')
#     file_object.write('第一次尝试写入文件第五行\n')
#     file_object.write('第一次尝试写入文件第六行\n')


Pra = 'E:\我的坚果云\文件\私人\Python\Testtxt\Practise.txt'

with open(Pra,'a')as file_object:
    i = 1
    n = ''
    while i==1 and n != 'exit':
        n = input('Please input your name: ')
        file_object.writelines(n + '\n')
        print(n)
