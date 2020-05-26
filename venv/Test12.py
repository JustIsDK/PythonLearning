# # try:
# #     print(5/0)
# # except ZeroDivisionError:
# #     print('你不能拿这玩意儿除以0啊！')
# print('接下来请输入两个数字，我会把他们相除\n')
# print("如果不想玩儿了，就输入 ‘离开’ 两个字就可以滚蛋了\n")
#
# while True:
#     fn = input('那么请输入第一个数字： ')
#     if fn == '离开':
#         break
#     print('\n')
#     sn = input('然后请输入第二个数字： ')
#     if sn == '离开':
#         break
#     print('\n')
#     try:
#         ansewer = int(fn) / int(sn)
#     except ZeroDivisionError:
#         print('不要调皮哦，0又不能作为除数~~\n')
#     else:
#         print(ansewer)

# PTXT = 'E:\我的坚果云\文件\私人\Python\Testtxt\Python_learn1.txt'
# try:
#     with open(PTXT)as file_object:
#         PY = file_object.read()
# except FileNotFoundError:
#     print('Sorry,the file:\n' + PTXT + '\nnot exist')


PTXT = ['E:\我的坚果云\文件\私人\Python\Testtxt\Python.txt','E:\我的坚果云\文件\私人\Python\Testtxt\Alice.txt','E:\我的坚果云\文件\私人\Python\Testtxt\PI.txt',
        'E:\我的坚果云\文件\私人\Python\Testtxt\Practise.txt','E:\我的坚果云\文件\私人\Python\Testtxt\Python_learn.txt']


def count_word(filename):
    try:
        with open(filename)as f_ob:
            PY = f_ob.read()
    except FileNotFoundError:
        print('Sorry,the file:\n' + filename + '\nnot exist')
    else:
        words = PY.split()
        num_words = len(words)
        print('This book has '+ str(num_words) + ' words.')

for PY in PTXT:
    count_word(PY)

# PTXT = ['E:\我的坚果云\文件\私人\Python\Testtxt\Python.txt','E:\我的坚果云\文件\私人\Python\Testtxt\Alice.txt','E:\我的坚果云\文件\私人\Python\Testtxt\PI.txt',
#         'E:\我的坚果云\文件\私人\Python\Testtxt\Practise.txt','E:\我的坚果云\文件\私人\Python\Testtxt\Python_learn.txt']
# miss = 'E:\我的坚果云\文件\私人\Python\Testtxt\missing.txt'
#
# def count_word(filename):
#     try:
#         with open(filename)as f_ob:
#             PY = f_ob.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = PY.split()
#         num_words = len(words)
#         print('This book has '+ str(num_words) + ' words.')
#
# for PY in PTXT:
#     count_word(PY)