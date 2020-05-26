#def hello(name):
#    '''打印hello world！'''
#    print('Hello '+ name.upper()+  ' World!')

#hello('DK')

# def puppy(name,type):
#     print('My '+type.title()+' \'s name  is '+name.title())
#
# puppy(type='wang',name='dog')

# def T(size,font='I Love You'):
#     print('Your T-shirt\'s size is '+size+' and your T-shirt\'s font is '+font.title())
#
# T('S','Hello')
# T(size='S',font='hello')
# T(size='S')

# def city(name,cou):
#     city_info={'name':name.title(),'cou':cou.title()}
#     print(city_info['name'],city_info['cou'])
#
# city('SH','China')
# city('SZ','china')


def ab(singer,ablum,num=''):
    info={'singer':singer,'ablum':ablum,'num':num}
    print(info['singer'],info['ablum'],info['num'])

while True:
    exit = str(input('请输入exit以便于退出： '))
    ss = str(input('请输入歌手名字： '))
    abb = str(input('请输入专辑名称： '))
    size = str(input('请输入此专辑中的歌曲数量： '))

    if ss == 'exit':
        break
    if abb == 'exit':
        break
    if size == 'exit':
        break

    if exit != 'exit':
        ab(ss,abb,size)
    else:
        break

# def show_magic(names):
#     for name in names:
#         print(name.title())
#
# def great(names):
#     ll = []
#     for name in names:
#         new = 'The Great'
#         new_name = new + ' '+name.title()
#         ll.append(new_name)
#     print(ll)
#     return ll
#
# magicnames = ['jay','JJ','lin','kver']
# #show_magic(magicnames[:])
# #show_magic(great(magicnames[:]))
# aa = great(magicnames)
# print(aa)


