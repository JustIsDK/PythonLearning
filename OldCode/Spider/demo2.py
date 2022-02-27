import requests
from bs4 import BeautifulSoup as bfs
import pandas as pd
from urllib.request import urlretrieve
import  os
baseurl = 'https://btbtt16.com/'
url = 'https://btbtt16.com/thread-index-fid-981-tid-4497137.htm'
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

def openurl(url,headers,title):
    r = requests.get(url=url, headers=headers)
    val = bfs(r.text, 'lxml')
    data = val.select('body > div > table:nth-child(2) > tbody > tr:nth-child(1) > td.post_td > div.attachlist > table > tbody > tr > td:nth-child(1) > a')
    print(data)
    # print(val)

    # downloadUrl = baseurl + data[0].get('href')
    # print(downloadUrl)
    # getFile(downloadUrl, title)


#cnblogs.com/aionwu/p/14952238.html   例子的网址,明天继续研究

openurl(url=url,headers=headers,title='test')