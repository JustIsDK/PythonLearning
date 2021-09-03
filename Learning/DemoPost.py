import unittest
import requests

class Testpost(unittest.TestCase):
    #创建话题
    def test_creat_topic(self):
        url = 'http://pqfavavk.dnat.tech/api/v1/topics'
        post_json = {
            "accesstoken":"ed9106c4-111f-45a8-9098-182154bb60ed",
            "title": "1",
            "tab": "ask",
            "t_content": "hello world",
            "topic_tags":""
        }
        #为什么没有专门定义headers,因为下面的data/json这两种处理方式就隐含了content-type的定义方式
        r = requests.post(url=url,data=post_json)#这样写,会把body转码成x-www-urlencoded编码形式
        # print(r.request.url)
        # print(r.request.body)
        # print(r.request.headers)
        print(r)

        r2 = requests.post(url=url,json=post_json)#json这样写,body会已json形式发出]
        # print(r2.request.body)
        print(r2)

