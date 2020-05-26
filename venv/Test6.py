# def sandwich(*everything):
#     for ss in everything:
#         print('你的三明治里要放这么些东西： ' + ss + '\n')
#
#
# sandwich('小龙虾','牛油果','么么哒')


# def build_profile(first,last,**user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['firstname'] = first
#     profile['lastname'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('华', '凯',location='上海',field='闵行')
# print(user_profile)

def car(maker,type,**other):
    info = {}
    info['maker'] = maker
    info['type'] = type
    for key,value in other.items():
        info[key] = value
    print(info)

# new_car = car('Audi','A4',cloor = 'blue',seat = 7)
# print(new_car)