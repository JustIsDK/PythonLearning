import unittest
import requests

domainurl = "http://47.103.35.77:3000/api/v1/topics"

class Testpost(unittest.TestCase):
    #token 为 null,发布失败
    def test_topic_tokenisnull(self):
        post_json = {
            "accesstoken" : "",
            "tab":"ask",
            "title" : "接口自动化提交测试",
            "content": "为什么会 400 呢?",
            "topic_tags":"",
            "_csrf":""
        }
        r = requests.post(url=domainurl,data=post_json)
        print(r.json())
        self.assertEqual(r.status_code,401)
        self.assertFalse(r.json()['success'])