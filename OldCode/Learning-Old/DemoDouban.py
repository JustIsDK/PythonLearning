import unittest
import requests
import os

class TestDoubanMoive(unittest.TestCase):

    def test_moive(self):
        get_url = "https://movie.douban.com/j/search_subjects"
        get_param = {
            "type": "movie",
            "tag": "华语",
            "page_limit": 50,
            "page_start": 0
        }
        # 定制请求头
        myheaders = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
        # 发送请求 headers=myheaders 定制请求头， headers 固定写法
        r = requests.get(url=get_url,params=get_param,headers=myheaders)
        print(r.request.headers) # 'User-Agent': 'python-requests/2.26.0'
        print(r.text)
        # 将服务器返回结果中的 url 图片保存到本地
        subjects = r.json()["subjects"]

        # 循环遍历每个结果
        for sub in subjects:
            #打印每个电影的标题和海报链接
            print(sub['title'],sub['cover'])
            #图片保存到本地
            if not os.path.exists('pngs'):
                os.mkdir('pngs')
            r = requests.get(sub['cover'])
            with open("pngs/"+sub['title']+'.jpg',mode='wb')as file:
                #content 把这个 cover 的链接下载下来,保存为上面规定的文件名
                file.write(r.content)