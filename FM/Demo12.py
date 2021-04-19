import unittest
import requests
import json


class NodeBlogTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_interface_result(self):
        urls = 'http://fuman-admin-stage.dongfangfuli.com/backend/product/productDec/getProductInfoByCondition'
        headers = {
            'Accept':'application/json',
            'admin-token':'ea6f152b-da59-4dec-86e5-8f4f784ec82f',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

        }
        d = json.dumps({"pageNum":1,"pageSize":20})
        res = requests.post(url=urls,data=d,headers=headers).json()
        self.assertEqual(res['code'],"004006")
        print(res)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

"""
主要测试 cnode社区的话题相关的功能
主要api包括：
1.  主题首页
"""
# # 引入第三方模块
# import requests
#
#
# def test_topic_page():
#     """
#     测试主题首页功能
#     get请求方法
#     url： http://49.233.108.117:3000/api/v1/topics
#     :return:
#     """
#     # 1. 发送get请求
#     url = 'http://49.233.108.117:3000/api/v1/topics'
#     getdata = {
#         "page": 1,
#         "tab": "ask",
#         "limit": 100,
#         "mdrender": "true"
#     }
#     res = requests.get(url=url, params=getdata)
#     print(res)
#     # 2.查看状态码
#     print('状态码：', res.status_code)
#     # 3. 查看json结果
#     print(res.json())
#
#     jsondata = res.json()
#     data = jsondata['data']
#     print(len(data))
#     assert len(data) == 1
#
#     for d in data:
#         # print(d['tab'])
#         assert d['tab'] == 'ask'
#         if d['tab'] != 'ask':
#             print('数据验证失败')
#
#
# def test_create_topic():
#     """
#     创建主题
#     :return:
#     """
#     create_url = "http://49.233.108.117:3000/api/v1/topics"
#     post_data = {"accesstoken": "8aac85ba-e4b2-4093-ac23-b4154fcca626",
#                  "title": "helloworld",
#                  "tab": "ask",
#                  "content": "xxxxxxxxxx"}
#     res = requests.post(url=create_url, data=post_data)
#
#     print(res.status_code)
#     print(res.json())
#
#
# def test_topic_detail():
#     """
#     主题详情
#     :return:
#     """
#     url = "http://49.233.108.117:3000/api/v1/topic/5f043909357c334168d7741d"
#     res = requests.get(url)
#     print(res.status_code)
#
#     print(res.json())
#
#     '''获取响应时间'''
#     r.elapsed.total_seconds()，单位是s