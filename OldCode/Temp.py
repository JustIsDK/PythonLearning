a = 'pid={商户ID}&type={支付方式}&out_trade_no={商户订单号}&notify_url={服务器异步通知地址}&return_url={页面跳转通知地址}&name={商品名称}&money={金额}&sitename={网站名称}&sign={签名字符串}&sign_type=MD5'

# a = 'act=order&pid={商户ID}&key={商户密钥}&out_trade_no={商户订单号}'
b = a.split('&')
print('{')
for i in b:
     d = i.split('=')
     print('"'+d[0]+'"'+':'+'"'+d[1]+'"'+',')

print('}')
# import random
#
# a = random.randint(00000000000000000,99999999999999999)
# print(a)
import time

now = time.time()

print(now)

a = {1,2,3}
b = {2,3}
