import unittest
import requests

domainurl = "http://47.103.35.77:3000/api/v1/topics"
token = '26b63ec9-4123-4893-8d9a-7d5e668e8b22'
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
        r = requests.post(url=domainurl,data=post_json,verify=False)
        print(r.json())
        self.assertEqual(r.status_code,401)
        self.assertFalse(r.json()['success'])

    # token值失效发布话题  话题发布失败 对失败信息添加断言
    def test_create_topic_with_error_token(self):
        post_json = {
            "accesstoken" : "26b63ec9-4123-4893-8d9a-7d5e668e8b23",
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
