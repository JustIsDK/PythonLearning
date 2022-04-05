# a = 'pid={商户ID}&type={支付方式}&out_trade_no={商户订单号}&notify_url={服务器异步通知地址}&return_url={页面跳转通知地址}&name={商品名称}&money={金额}&sitename={网站名称}&sign={签名字符串}&sign_type=MD5'
#
# # a = 'act=order&pid={商户ID}&key={商户密钥}&out_trade_no={商户订单号}'
# b = a.split('&')
# print('{')
# for i in b:
#      d = i.split('=')
#      print('"'+d[0]+'"'+':'+'"'+d[1]+'"'+',')
#
# print('}')
# import random
#
# a = random.randint(00000000000000000,99999999999999999)
# print(a)
# import time
#
# now = time.time()
#
# print(now)

# a = {1,2,3}
# b = {2,3}

# print(sum([i for i in range(1,101)]))

# a=0
# while a<3 :
#     b = input('Please input your pwd: ')
#     if b == 'aaa':
#         print('Login Success')
#     else :
#         a = a+1
#         print('Wrong PWD')
#
# print('You have beening wrong for three times')


# for i in range(3):
#     password = int(input("plesae write your password: "))
#     if password == 8888:
#         print("输出密码正确，成功进入系统")
#         break
#     else:
#         if i == 2:
#             print("你尝试次数已经最大，程序结束")
#         else:
#             print(f"密码错误，请重新输入，还剩{2-i}次机会")