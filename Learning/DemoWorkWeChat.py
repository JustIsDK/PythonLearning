#订一个会议室
import unittest

import requests

# test_data={
#     "accesstoken":""
# }

access_token = []

#发现问题,test_X,这个x会被unittest取到字幕顺序来作为执行顺序,故可以加上数字来定他的顺序,否则出现我一样token取不到的情况
class TestMeetingRoom(unittest.TestCase):
    def test_1get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        get_param = {
            'corpid':'ww88fc20d87e4cdfa1',
            'corpsecret':'8kZYaPdkie4nuh3itIwhgUKpam5Xyoq5hU4uivaswp4'
        }
        r = requests.get(url=url,params=get_param)
        # token = r.json()['access_token']
        # test_data['accesstoken'] = token
        access_token.append(r.json()['access_token'])
        self.assertIsNotNone(access_token[0])


    def test_2add_meetingroom(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={access_token[0]}"
        postdata = {
            "name": "1809998F-会议室",
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
        print(r.json())



