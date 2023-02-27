import requests
import json
import time
import random

def blf():#布洛芬库存查询
   url = "https://h5.m.youzan.com/wscgoods/tee-app/detail.json?app_id=wx6aae272c6a3eaead&from_uuid=pfjknyZhBjmZci61671180216007&subKdtId=0&scene=1074&fullPresaleSupportCart=true&is_share=1&prefetchKey=prefetch%3AGoodsDetail%3A1671460955133&platform=weixin&alias=3f20lko7byn1utd&withoutSkuDirectOrder=1&isGoodsWeappNative=1&shopAutoEnter=1&kdt_id=116099074&client=weapp&oid=0&ump_alias=&ump_type=&activityId=&activityType="

   payload = {}
   headers = {
      'Host': 'h5.m.youzan.com',
      'accept': '*/*',
      'content-type': 'application/json',
      'extra-data': '{"version":"3.80.3","clientType":"weapp-miniprogram","client":"weapp","bizEnv":"","ftime":1671460873409}',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac',
      'referer': 'https://servicewechat.com/wx6aae272c6a3eaead/79/page-frame.html',
      'accept-language': 'zh-CN,zh-Hans;q=0.9',
      'Cookie': '_kdt_id_=116099074'
   }

   response = requests.request("GET", url, headers=headers, data=payload)

   # print(response.json())

   num = response.json()['data']['goodsData']['skuInfo']['skuStocks'][0]["stockNum"]
   title = response.json()['data']['goodsData']['goods']['title']
   return num,title  #返回库存数量和标题名称

# blf()


def send_wechat(msg,title):#一对一推送
   token = '2c7c606fa2b944558c709e7b877ee6b6'  # 推送后台的token
   title = title
   content = msg
   template = 'html'
   url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
   r = requests.get(url=url)
   if r.json()['code'] == 200:
      print('信息发送成功\n')


def send_wechats(msg,title):#一对多推送
   token = '2c7c606fa2b944558c709e7b877ee6b6'  # 推送后台的token
   title = title
   content = msg
   template = 'html'
   topic = '123456'  #群组编号
   url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}&topic={topic}"
   r = requests.get(url=url)
   if r.json()['code'] == 200 :
      print('信息发送成功\n')


# send_wechat('测试消息')

flag = True #初始化循环标识
while flag == True:
   result = blf()[0] #返回库存
   res = int(result) #类型转换,py 实际不用这么做也行
   if res >1000: #大库存才发提醒
      title = f'修正小程序搜索: {blf()[1][0:6]} ,外观是白盒+红人'
      msg = (f'这次是另一种布洛芬,外盒是白色,封面有红色人物轮廓\n'
             f"这次放出了 {res} 的库存\n"
             f"轮询会休息30分钟,然后开始下一次的轮询~\n"
             f"抢药全凭本事,祝君好运~~~~~")
      send_wechats(msg,title)
      timesleep = 1800
      print(f"休息 {timesleep} 秒\n")
      time.sleep(timesleep)
      # flag = False
   else:
      if res > 0:
         print(f"目前的库存为 {res} ,很少,不妨试试看?\n")
      else:
         print("啥也没有,再等等\n")
      timesleep = random.randint(2,10)
      print(f"休息 {timesleep} 秒\n")
      time.sleep(timesleep)