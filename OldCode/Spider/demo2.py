import requests
from bs4 import BeautifulSoup as bfs
import pandas as pd
import re
from urllib.request import urlretrieve
import  os
baseurl = 'https://btbtt16.com/'
url = 'https://btbtt16.com/thread-index-fid-981-tid-4497137.htm'
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

def firststep(url,headers):
    r = requests.get(url=url, headers=headers)
    #请求url获取html
    soup = bfs(r.text, 'lxml')
    #用lxml解析成为对象
    data = soup.select('td >div[class="attachlist"] >table >tr >td >a[rel = "nofollow"]')
    #使用xpath找到目标列表
    dwl = []
    #新建空字典用来存放下载链接，其实用列表应该也足够了
    for i in range(len(data)):
        #循环取列表中的项
        newurl = baseurl + str(data[i].get('href'))
        #获取href属性的值，也就是种子的链接url
        filename = str(data[i].text[61:63])
        #截取种子的名字
        dwl.append(newurl)
        #为字典赋值，截取的标号：新链接
        print(filename+':'+newurl)
        print()

    # print (dwl)
    #打印出新的列表
# def getfile(url):

#
# def nextstep(downloadlinks):
#     for



firststep(url=url,headers=headers)