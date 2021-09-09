import unittest
from ddt import ddt,data
import requests

corpid = "ww88fc20d87e4cdfa1"
corpsecret = "8kZYaPdkie4nuh3itIwhgUKpam5Xyoq5hU4uivaswp4"


test_data={
    "token":""
}


@ddt
class TestDDT(unittest.TestCase):
    # @data(10,5,4,8) #四个测试数据
    # def test_datas(self,test_value):
    #     print('value is ',test_value)
    #     self.assertGreater(test_value,5)
    def test_1get_token(self):
        """
        获取token值
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        res = requests.get(url)
        # 添加断言
        self.assertIn("access_token", res.json())
        # 更改testdata 的值
        test_data["token"] = res.json()["access_token"]  # 实现往下游传参


    @data("1234567890123456789012345678901","18F-会议室")
    def test_2add_meetingroom(self,meeting_name):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={test_data['token']}"
        postdata = {
            "name": f"{meeting_name}",
            "capacity": 10,
            "city": "深圳",
            "building": "腾讯大厦",
            "floor": "18F",
            "equipment": [1, 2, 3],
            "coordinate":
                {
                    "latitude": "22.540503",
                    "longitude": "113.934528"
                }
        }
        r = requests.post(url=url,json=postdata)
        self.assertIsNot(r.json()['errmsg'],'ok')




