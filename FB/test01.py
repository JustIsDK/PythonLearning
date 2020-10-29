with open(r'D:\Code\file\test.txt','r',encoding='utf-8') as file1:
    fileread = file1.read()
    print(fileread)
    file1.close()


# with open(r'D:\Code\file\test.txt', 'w', encoding='utf-8') as file1:
#         file1.write('一号 11 22 33 44\n')
#         file1.write('二号 55 25 63 4\n')
#         file1.close()