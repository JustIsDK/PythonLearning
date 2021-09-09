#订一个会议室
import unittest
import random
import requests

test_data={
    "accesstoken":"",
    "meetingroom_id": 0
}

access_token = []

corpid='ww88fc20d87e4cdfa1'
corpsecret='8kZYaPdkie4nuh3itIwhgUKpam5Xyoq5hU4uivaswp4'

#发现问题,test_X,这个x会被unittest取到字幕顺序来作为执行顺序,故可以加上数字来定他的顺序,否则出现我一样token取不到的情况
class TestMeetingRoom(unittest.TestCase):
    def test_1get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        get_param = {
            'corpid':{corpid},
            'corpsecret':{corpsecret}
        }
        r = requests.get(url=url,params=get_param)
        token = r.json()['access_token']
        test_data['accesstoken'] = token
        # access_token.append(r.json()['access_token'])
        # self.assertIsNotNone(access_token[0])
        self.assertIsNotNone(test_data['accesstoken'])


    def test_2add_meetingroom(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={test_data['accesstoken']}"
        postdata = {
            "name": f"{random.randint(1000,10000)}-会议室",
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
        self.assertEqual(r.json()['errmsg'],'ok')
        self.assertTrue(r.json()['meetingroom_id']>0)
        test_data['meetingroom_id'] = r.json()['meetingroom_id']
        # print(test_data['meetingroom_id'])


    def test_3query_meetingroom(self):
        '''
        查询会议室
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/list?access_token={test_data['accesstoken']}"
        postdata = {
            "city": "深圳",
            "building": "腾讯大厦",
            "floor": "18F",
            "equipment": [1, 2, 3]
        }
        r = requests.get(url=url,params=postdata)
        meetingroomlist = r.json()['meetingroom_list']
        mids = []
        for meet in meetingroomlist:
            mids.append(meet['meetingroom_id'])
        self.assertIn(test_data['meetingroom_id'],mids)

    def test_4edit_meetingroom(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={test_data['accesstoken']}"
        postdata = {
          "meetingroom_id":test_data["meetingroom_id"],  # test_data["meetingroom_id"] 参数传递
          "name":f"会议室-{random.randint(1000,100000)}",
          "capacity":10,
          "city":"深圳",
          "building":"腾讯大厦",
          "floor":"18F",
          "equipment":[1,2,3],
          "coordinate":
          {
            "latitude":"22.540503",
            "longitude":"113.934528"
          }
        }
        r = requests.post(url=url, json=postdata)
        # 断言
        self.assertEqual(r.json()["errmsg"], "ok")

    def test_5delete_meetingroom(self):
        '''
        删除会议室
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/del?access_token={test_data['accesstoken']}"
        postdata = {
            "meetingroom_id": test_data["meetingroom_id"],
        }
        r = requests.post(url=url, json=postdata)
        self.assertEqual(r.json()['errmsg'], 'ok')





