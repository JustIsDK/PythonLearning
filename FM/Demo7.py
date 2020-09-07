# class User:
#     name = "xiaoming"
#     age = 20
#
#     def update_user_info(self,newname,newage):
#         self.name = newname
#         self.age = newage
#
# user = User()
# user.update_user_info('xiaowang',25)
# print(user.name)


# plist = [{
#     "name": "coke",
#     "price": 3
# }, {
#     "name": "apple",
#     "price": 10
# }]
# while True:
#     p = input("请输入购买的商品:")
#
#     for list in plist:
#         if list['name'] == p:
#             break
#     else:
#         print(f'您输入的商品{p}不在我们的商品列表中，请检查')
#
# code = '1234'
# num = 0
# while num < 3:
#     mima = input('请输入你的密码: ')
#
#
#     if mima != code:
#         print('密码错误')
#         print(f'您已尝试第{num}次')
#         num = num + 1
#         if num == 3:
#             print(f'已经尝试{num}次，请明日再试')
#             break
#     else:
#         print('输入正确')
#         break

#就是个注释

#
# def area(x):
#     s = 3.14 * x**2
#     return s
#
#
# print(area(3))