import requests
import json
import time
import random

def blf():#布洛芬库存查询
   url = "https://h5.m.youzan.com/wscgoods/tee-app/detail.json?app_id=wx6aae272c6a3eaead&kdt_id=116099074&alias=26wys8v278yqad0&oid=0&scene=1089&ump_alias=&ump_type=&activityId=&activityType=&subKdtId=0&fullPresaleSupportCart=true&platform=weixin&client=weapp&isGoodsWeappNative=1&withoutSkuDirectOrder=1"

   payload = ""
   headers = {
      'extra-data': '{"version":"3.80.3","clientType":"weapp-miniprogram","client":"weapp","bizEnv":"","ftime":1671171944945}',
      'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
      'content-type': 'application/json'
   }

   response = requests.request("GET", url, headers=headers, data=payload)

   num = response.json()['data']['goodsData']['skuInfo']['skuStocks'][0]["stockNum"]
   return num


def send_wechat(msg):#一对一推送
   token = '2c7c606fa2b944558c709e7b877ee6b6'  # 前边复制到那个token
   title = '抢药提醒'
   content = msg
   template = 'html'
   url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
   print(url)
   r = requests.get(url=url)
   print(r.text)


def send_wechats(msg):#一对多推送
   token = ' 2c7c606fa2b944558c709e7b877ee6b6'  # 前边复制到那个token
   title = '抢药提醒'
   content = msg
   template = 'html'
   topic = '1'
   url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}&topic={topic}"
   print(url)
   r = requests.get(url=url)
   print(r.text)

# send_wechat('测试消息')

flag = True #初始化循环标识
while flag == True:
   result = blf() #返回库存
   res = int(result) #类型转换,py 实际不用这么做也行
   if res >10000: #大库存才发提醒
      msg = (f"库存比较多,这次放出了 {res} , 赶紧抢吧!!!!!!!!!!!\n轮询会休息五分钟,然后开始下一次的轮询~\n 抢药全凭本事,祝君好运~~~~~")
      send_wechats(msg)
      timesleep = 300
      print(f"休息 {timesleep} 秒\n")
      time.sleep(timesleep)
      # flag = False
   else:
      print("继续查询\n")
      if res > 0:
         print(f"目前的库存为 {result} ,很少,不妨试试看?\n")
      else:
         print("啥也没有,再等等\n")
      timesleep = random.randint(30,50)
      print(f"休息 {timesleep} 秒\n")
      time.sleep(timesleep)