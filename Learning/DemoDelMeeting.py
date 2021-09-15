"""
每次进行测试，产生了大量垃圾数据， 比如在做会议室管理的接口中，
每次创建大量的会议室，现在要把所有的会议室都清空
"""
import unittest
from ddt import ddt,data
import requests

corpid = "ww88fc20d87e4cdfa1"
corpsecret = "8kZYaPdkie4nuh3itIwhgUKpam5Xyoq5hU4uivaswp4"

test_data={
    "accesstoken":"",
    "meetingroom_id":0,
    'meetingrooms':[]
}

url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
res = requests.get(url)
# 添加断言
# 更改testdata 的值
token = res.json()["access_token"]
test_data["accesstoken"] = token  #实现往下游传参

url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/list?access_token={test_data['accesstoken']}"
res = requests.post(url)
print(res.json())
print(len(res.json()["meetingroom_list"]))
for meeting in res.json()["meetingroom_list"]:
    test_data['meetingrooms'].append(meeting["meetingroom_id"])
print(f'所有的rooms： {test_data["meetingrooms"]}')



@ddt
class TestDELMeetingRoom(unittest.TestCase):

    @data(*test_data["meetingrooms"])
    def test_3del_rooms(self,roomid):
        """
        删除会议室 {roomid}
        :param roomid:
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/del?access_token={test_data["accesstoken"]}'
        del_data = {
            "meetingroom_id":roomid,
        }
        res = requests.post(url,json=del_data)

        self.assertEqual(res.json()["errmsg"],"ok")