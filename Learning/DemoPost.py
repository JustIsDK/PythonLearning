import unittest
import requests

domainurl = 'http://47.103.35.77:3000'

class Testpost(unittest.TestCase):
    #创建话题   不知道为什么,永远 403 和 400,和教程一样,这个暂且不论
    def test_creat_topic(self):
        url = domainurl +'/topic/create'
        post_json = {
            "accesstoken" : "26b63ec9-4123-4893-8d9a-7d5e668e8b22",
            'tab':'ask',
            'title' : '接口自动化提交测试',
            't_content': '为什么会 400 呢?',
            'topic_tags':'',
            '_csrf':''
        }
        #为什么没有专门定义headers,因为下面的data/json这两种处理方式就隐含了content-type的定义方式
        r = requests.post(url=url,data=post_json)#这样写,会把body转码成x-www-urlencoded编码形式
        print(r.request.url)
        print(r.request.body)
        print(r.request.headers)
        print(r)

        # r2 = requests.post(url=url,json=post_json)#json这样写,body会已json形式发出]
        # # print(r2.request.body)
        # print(r2)

