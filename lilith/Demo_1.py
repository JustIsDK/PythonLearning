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



'''
批量获取测试计划名称
'''
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

list = {
1057,
1072,
1119,
1142,
1154,
1175
        }

# for i in list:
#     getPlanName(i)


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print('')