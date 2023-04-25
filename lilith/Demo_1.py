'''
status = 33
def matchdemo(status):
    match status:
        case 11|33:
            print(11)
        case 22:
            print(22)
        case _:
            print("nothing")

matchdemo(status)

'''
import json

import requests

'''
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

'''
def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()

def fib2(n):
    a,b = 0,1
    result = []
    while a<n:
        result.append(a)
        a,b = b,a+b
    print(result)

def is_unique(string):
    if string is None:
        return False
    return len(set(string))==len(string)


'''
sort() 和 sorted() 的区别：sort() 应用在 list 列表中
而 sorted() 可以对所有可迭代的对象进行排序操作
'''

def is_queue(str1,str2):
    if str1 is None or str2 is None:
        return False
    return sorted(str1)==sorted(str2)


def plusOne(digits:list[int]) -> list[int]:
    num = ''
    for i in digits:
        num  = num + str(i)
    newlist = int(num) + 1
    newlist = str(newlist)
    newlist2 = []
    for i in newlist:
        newlist2.append(i)
    print(newlist2)



projectList = ["https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=998&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=969&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=967&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=962&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=961&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=960&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=959&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=958&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=957&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=916&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=915&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=914&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=913&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=912&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=911&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=910&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=909&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=908&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=907&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=906&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=905&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=904&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=903&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=902&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=901&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=900&planStatus=2",
"https://testcase-xmind.lilithgames.com/View?allCaseNum=6&planId=889&planStatus=2"]
import re
from urllib.parse import urlparse, parse_qs
def getId(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    plan_id = query_params.get("planId", [])[0]
    return int(plan_id)

def getPlanName(projectId):
    url = f"https://main.lilithgames.com/api/testcase-xmind/plan/info/{projectId}?projectId=PlatformTest"

    payload={}
    headers = {
       'authority': 'main.lilithgames.com',
       'dnt': '1',
       'jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzYWx0IjoiZGQxOWY0ZWQ5MjkxNDMwZDg0NGQ0ODkxNTc5OTViNWMiLCJmdWxsbmFt'
              'ZSI6IuWNjuWHryIsImV4cCI6MTY4MzI1Mzk1OCwiZW1haWwiOiJka2h1YUBsaWxpdGguY29tIn0.CHdgwCoJhD7E1M9N-sMfh4G3DGo9t'
              '83DWSfgvQGL9lpqp6KayrKDs0UfgMepJlb5dpwf6yMpBhGzp_dOWXn9Wi42MS9QqFuyCo5Xi4uWSKT7aCNwf5kLyn9_ZyMHBZL-4DiglaIswtzdzoFLosvgCVro2UJRH5k6CrjhfeDkP1WnsJoeDfWqf5QC8dfRBE1B43FdbN-9TMX4vio3iP1M29cdPMGTmIq9zrmk85Wtc_gD09ag8pOBcVmNz_ouS1cxB7_Xr9q4vTCU_tWsKZ1-RuGSHuMGYmxWhhwV2hNNxMHHBz0t_at9X1rTzk01xBYTLiKbw4E3YNyToXZgCRFEZw',
       'Cookie': '_ga=GA1.1.201447006.1672993537; _ga_785SBE4X1E=GS1.1.1672993536.1.1.1672993555.0.0.0; _ga_EFJK0JQ14G=GS1.1.1673503050.1.0.1673503057.0.0.0; qa_test_at=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzYWx0IjoiZGQxOWY0ZWQ5MjkxNDMwZDg0NGQ0ODkxNTc5OTViNWMiLCJmdWxsbmFtZSI6IuWNjuWHryIsImV4cCI6MTY4MzI1Mzk1OCwiZW1haWwiOiJka2h1YUBsaWxpdGguY29tIn0.CHdgwCoJhD7E1M9N-sMfh4G3DGo9t83DWSfgvQGL9lpqp6KayrKDs0UfgMepJlb5dpwf6yMpBhGzp_dOWXn9Wi42MS9QqFuyCo5Xi4uWSKT7aCNwf5kLyn9_ZyMHBZL-4DiglaIswtzdzoFLosvgCVro2UJRH5k6CrjhfeDkP1WnsJoeDfWqf5QC8dfRBE1B43FdbN-9TMX4vio3iP1M29cdPMGTmIq9zrmk85Wtc_gD09ag8pOBcVmNz_ouS1cxB7_Xr9q4vTCU_tWsKZ1-RuGSHuMGYmxWhhwV2hNNxMHHBz0t_at9X1rTzk01xBYTLiKbw4E3YNyToXZgCRFEZw',
       'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json()['data']['planName'])


# for i in projectList:
#     getPlanName(getId(i))