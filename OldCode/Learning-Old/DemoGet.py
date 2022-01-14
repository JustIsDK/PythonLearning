import unittest
import requests
# #类的级别可以当做模块级别
# class TestAPI(unittest.TestCase):
#     #函数级别可以当做用例级别
#     def test_topic(self):
#         self.assertTrue(True)
#
#     def test_topic_false(self):
#         self.assertTrue(True)
#
# class TestCase(unittest.TestCase):
#     def test_demo1(self):
#         pass
#
#     def test_demo2(self):
#         pass
#
#
# #执行 双等号==  以及main的()不要忘了
# if __name__=='__main__':
#     unittest.main()
#简单的接口请求,基本使用方法
class Testcnodeapi(unittest.TestCase):
    #简单的返回
    def test_topic_page(self):
        #配置请求参数,设定为最多1个
        get_param = {
            "limit":1
        }
        #请求中带上这个参数,确保返回的只有1个
        r = requests.get(url='http://pqfavavk.dnat.tech/api/v1/topics',params=get_param)
        print(r.status_code)
        print(r.json())
        #加上断言assert
        self.assertEqual(r.status_code,200)
        #取到返回体重的data部分,这里返回的对象是列表
        data = r.json()["data"]
        print(data)
        self.assertEqual(len(data),1)
        #需要从列表中取到具体的值,这个值就是一条记录,再从这个值中取到tab的值
        for dat in data:
            self.assertEqual(dat['tab'], 'share')


