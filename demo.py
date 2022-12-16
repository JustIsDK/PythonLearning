import requests
import json

url = "https://h5.m.youzan.com/wscgoods/tee-app/detail.json?app_id=wx6aae272c6a3eaead&kdt_id=116099074&alias=26wys8v278yqad0&oid=0&scene=1089&ump_alias=&ump_type=&activityId=&activityType=&subKdtId=0&fullPresaleSupportCart=true&platform=weixin&client=weapp&isGoodsWeappNative=1&withoutSkuDirectOrder=1"

payload = ""
headers = {
   'extra-data': '{"version":"3.80.3","clientType":"weapp-miniprogram","client":"weapp","bizEnv":"","ftime":1671171944945}',
   'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
   'content-type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()['data']['goodsData']['skuInfo']['skuStocks'][0]["stockNum"])