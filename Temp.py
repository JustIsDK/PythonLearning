# a = input('Please input your string: ')
# sp = input('Please tell me how to split: ')
# b = a.split(sp)
# print('{')
# for i in b:
#      d = i.split('=')
#      print('"'+d[0]+'"'+':'+'"'+d[1]+'"'+',')
#
# print('}')
# 用来处理表单转化为json
# import random
#
# a = random.randint(00000000000000000,99999999999999999)
# print(a)
# import time
#
# now = time.time()
#
# print(now)
import json


# a = {1,2,3}
# b = {2,3}

# print(sum([i for i in range(1,101)]))

# a=0
# while a<3 :
#     b = input('Please input your pwd: ')
#     if b == 'aaa':
#         print('Login Success')
#     else :
#         a = a+1
#         print('Wrong PWD')
#
# print('You have beening wrong for three times')



#---------------------------------------------
def ifpwdright():
    for i in range(3):
        password = int(input("plesae write your password: "))
        if password == 8888:
            print("输出密码正确，成功进入系统")
            break
        else:
            if i == 2:
                print("你尝试次数已经最大，程序结束")
            else:
                print(f"密码错误，请重新输入，还剩{2-i}次机会")


#---------------------------------------------


# lst = [i for i in range(1,10)]
# lst2 = [i*2 for i in range(1,6)]
# print(lst2)
def mymax(x,y):
    # 简单的写法
    m = x if x>y else y
    print(m)

# mymax(1,2)

#---------------------------------------------

"""
内部函数包含对外部作用域的引用而非全局作用域的引用，该内部函数就是闭包函数
"""

def fun():
    name = 'jack'
    #这样的情况下，inner就是闭包函数
    def inner():
        print(name)
    print(inner.__closure__)
    # 在外面调用内部的inner该怎么用
    return inner
#
# f = fun()
# f() #==>inner()

#假如直接调用fun()则不会直接返回inner的结果,需要使用上述的方法才可以
# fun()
#如何判断是否是闭包呢,用__closure__

#---------------------------------------------

"""
匿名函数-功能简单的一句话函数
"""

def fun(x):
    return x**x


# fun = lambda n:n**n
#
# print(fun(3))

#---------------------------------------------

"""
递归函数  经典例子斐波那契数列 但是py的递归深度只有997
但是我们可以通过sys库的set方法来改变递归深度
"""

import sys
# print(sys.setrecursionlimit(100000))
def f(n):
    print(n)
    n += 1
    f(n)

def age(n):
    if n ==1:
        return 18
    else:
        return age(n-1)+2



def fib(n):
    if n==1 or n==2:
        return n
    elif n>=3:
        return fib(n-1) + fib(n-2)
    else:
        return -1



#---------------------------------------------

"""
装饰器的理解
以下操作便实现了装饰器的原理
不改变原函数的功能下增加功能
"""

import time

def funny():
    time.sleep(1)
    print("It`s Funny")


def timer(fun):
    #这里就是闭包,返回的是inner函数
    def inner():
        start = time.time()
        fun()
        print(time.time()-start)
    return inner
#
# #这里调用timer传入的参数就是funny函数,返回的是inner函数
# funny = timer(funny)
# #这里就是在调用inner函数,而inner函数又调用了funny函数
# funny()
#------------------------------------------------------

"""
如果使用装饰器的形式的话可以改成下面这样
"""

import time
def timer(fun):
    def inner():
        start = time.time()
        fun()
        print(time.time()-start)
    return inner

@timer
def funny():
    time.sleep(1)
    print("It`s Funny")
#
# funny()

#---------------------------------------------

"""
迭代器和生成器
"""

from _collections_abc import Iterable

def iterablepractise():
    lst = [i for i in range(1,11)]
    t = (1,2,3,4)
    d = {1:2,3:4}
    s = {1,2,3,4}

    print(isinstance(d,Iterable))

# 这样就能知道这个迭代器比普通的列表方法多出了那些方法
# print(set(dir([1,2].__iter__()))-set(dir([1,2])))
# ier1 = [1,2,3].__iter__()
# #这个length的方法是无法匹配出来的,需要手动输入
# print(ier1.__length_hint__())

#---------------------------------------------

"""
生成器函数 generator
"""

def fun():
    a = 1
    print('i have a')
    #和return的区别在于return会结束当前运行,后面的不会运行,而yield不会
    #有这个关键字就是生成器函数
    yield a
    b = 2
    print('i have b')
    yield b
#
# funny = fun()
# print(funny)
# print(next(funny))
# print(next(funny))

#---------------------------------------------
def demo11():
    s = 'aAsmr3idd4bgs7Dlsf9eAF'

    s1 = ''

    for i in s:
        if i.isdigit():
            s1 +=  i

    print(s1)


#---------------------------------------------

"""
输入一行字符,统计其中有多少个单词，每两个单词之间以空格隔开。
"""

def calc():
    flag = '1'
    while flag == '1':
        a = input('Please input you words: ')
        res = a.split(' ')
        res1 = []
        for i in res:
            if i == '':
                pass
            else:
                res1.append(i)
        num = len(res1)
        print(f'There are {num} words')
        flag = input('If you want to continue,please input "1" \n'
                     'If you want to exit,please input "2"\n'
                     'Please input your answer: ')


#------------------------------------------------------------------------

'''
生成年月日
'''

import random
def monthday():
    bigm = [1,3,5,7,8,10,12]
    smallm = [4,6,9,11]
    specialm = 2
    year = random.randint(1960,2022)
    month = random.randint(1,12)
    if month in bigm:
        day = random.randint(1,32)
    elif month in smallm:
        day = random.randint(1,31)
    elif month == specialm:
        day = random.randint(1,29)
    if day <=9:
        day = '0'+str(day)
    if month <=9:
        month = '0'+str(month)
    return (str(year)+' '+str(month)+' '+str(day))



#------------------------------------------------------------------------
'''
董小娜的练习
'''
def practise():
    i = [{'a':1,'b':[11,22,33,55]},[111,222,333],{121,212,313,414}]
    # s=i[1]
    # s[1]=22
    s=i[0]['b']
    s[1]=44
    print(s)

# 以sep作为分隔符，将seq所有的元素合并成一个新的字符串
# a = ['1','2','3','4','5']
#
# print(':'.join(a))

#------------------------------------------------------------------------
# import pytest
# import requests
# limit = [1,50,51]
# tab = ['ask','job','share']
# tab_limit_data=[]
# for i in tab:
#     for a in limit:
#         ex_tab = i
#         if a >=51:
#             ex_limit = 50
#         else:
#             ex_limit = a
#         tab_limit_data.append([i,a,ex_tab,ex_limit])
# @pytest.mark.parametrize('tab,limit,ex_tab,ex_limit',tab_limit_data)
# def test_topic(tab,limit,ex_tab,ex_limit):
#     url = 'http://47.100.175.62:3000/api/v1/topics'
#     body = {
#         'tab':tab,
#         'limit':limit
#     }
#     res = requests.get(url,params=body)
#     print(res.json())
#     for i in res.json()['data']:
#         assert i['tab'] == ex_tab
#     assert len(res.json()['data']) == ex_limit
#     # print(tab,limit,ex_tab,ex_limit)


#------------------------------------------------------------------------
def pingshan():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = []
    for i in a:
        if i%2 != 0 :
            b.append(i)
    print(b)

#------------------------------------------------------------------------
def phonenum():
    a = [1,0,7,6,5,4,9,3]
    b = [0,4,3,1,2,0,5,4,3,6,7]
    c = []
    d = '联系方式为: '
    for i in b :
        c.append(a[i])
        d = d + str(a[i])
    print(c)
    print(d)

# ------------------------------------------------------------------------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# x = Person("Bill", "Gates")
# x.printname()

# class Student(Person):
#     pass
# y=Student('yiyi','haha')
# y.printname()

# ------------------------------------------------------------------------

'''
百度面试题
生成器的知识
g被赋值之后就是个生成器
for循环中的g只是被赋值的状态,并没有被调用
在最后的list(g)时才被调用,这个时候的g已经被赋值了3次
且n也等于了5
那么反过来拆三层g的调用,最里面一层的g = (add(5,i) for i in g)
i的值为g生成的0 1 2 3,所以这一层的左侧g被赋值为 5 6 7 8
且作为下一层的右边g,就变成n5  i 5 6 7 8
得出 10 11 12 13赋值给左边g
依此类推 n5 i 10 11 12 13
得出最后 15 16 17 18
如上
'''
def add(n,i):
    return n+i
    print(n,i,n+i)

# def test():
#     for i in range(4):
#         yield i
#
# g = test()
#
# for n in [10,1,5]:
#     g = (add(n,i) for i in g)
# print(list(g))

# s =''
# a = s.split('、')
# man = 0
# for i in a:
#     man+=1
# print(man)


'''
编写一个函数，接受一个字符串作为参数，然后返回该字符串中每个单词的反转字符串。例如，输入"Hello World"，输出"olleH dlroW"。
'''
text = 'Hello world'
def reverse_word(words):
    words_list = words.split(' ')
    reverse_word_list = [word[::-1] for word in b]
    print(' '.join(c))


'''
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
单字母可以,多字母的字符串就失效
在 sort 中加上  key=str.lower  可以解决这个问题
'''
def sort_string():
    total_line = input('请输入行数: ')
    sum_list = []
    for i in range(int(total_line)):
        sum_list.append(input('请输入字符,仅限英文大小写: '))
    sum_list.sort(key=str.lower)
    for i in sum_list:
        print(i)


'''
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
'''
def calc_binary(numbers):
    num_bin = bin(numbers)
    print(num_bin.count('1'))


'''
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
'''
def calc_last_string():
    new_string = input('Please input your string: ')
    new_list = new_string.split()
    print(len(new_list[-1]))


'''
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
'''
def calc_target_num():
    new_string = input().lower()
    target = input().lower()
    print(new_string.count(target))

'''
明明生成了
N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，
把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
'''
def set_list():
    num_amount = int(input())
    first_list = []
    for i in range(int(num_amount)):
        first_list.append(input())
    second_list = set(first_list)
    second_list = list(second_list)
    for i in range(len(second_list)):
        second_list[i] = int(second_list[i])
    second_list.sort()
    for i in second_list:
        print(i)


'''
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
'''
def split_string():
    new_string = input()
    if new_string != '':
        if len(new_string)%8 != 0:
            new_string += '0'* (8 - len(new_string)%8)
        split_string = [new_string[i:i+8] for i in range(0,len(new_string),8)]
        after_string = ''
        for i in split_string:
            print(i)
    else:
        pass


'''
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
int(s,16)  16->10 进制
'''
def tentosix():
    i = input()
    print(int(i,16))


'''
输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 )
'''
import math
def split_number():
    num = int(input())
    newnum = num
    for i in range(2,int(math.sqrt(newnum))+1):
        while newnum % i == 0:
            print(i,end=' ')
            newnum = newnum // i
    if newnum != 1:
        print(newnum)

'''
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
直接取 int 的话,会忽略后面的小数,所以加上 0.5,如果本身小数部分已经大于等于 0.5,那么加上之后就会往上加一个数,这样取整之后就是向上取整了
'''
def rounding():
    num = float(input())
    num = int(num+0.5)
    print(num)


'''
数据表记录包含表索引index和数值value（int范围的正整数）
请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算
输出按照index值升序进行输出。
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开
'''
def mergelist():
    n = int(input())
    dic = {}

    # idea: 动态建构字典
    for i in range(n):
        line = input().split()
        key = int(line[0])
        value = int(line[1])
        dic[key] = dic.get(key, 0) + value  # 累积key所对应的value

    for each in sorted(dic):  # 最后的键值对按照升值排序
        print(each, dic[each])



'''
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。
'''
def reversenum():
    num = input()
    newlist = [i for i in num]
    if newlist[-1] == '0':
        print('over')
    else:
        newlist = newlist[::-1]
        newlist2 = []
        for i in newlist:
            if i not in newlist2:
                newlist2.append(i)
        newstring = ''
        for i in range(len(newlist2)):
            newstring += newlist2[i]
        print(newstring)


'''
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )
换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。
'''
def calcstringnum():
    cstring = input()
    cstring = list(set(list(cstring)))
    print(len(cstring))


'''
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
'''
def reversestring():
    newstring = input()
    print(newstring[::-1])


'''
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
'''
def reversesentence():
    sentence = input()
    sentence = sentence.split(' ')
    sentence.reverse()
    print(' '.join(sentence))



'''
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无

如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，
用整数 1 ~ 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。
满意度是指所购买的每件物品的价格与重要度的乘积的总和.

输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。
如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
'''
def calchapppy():
    moneyandcount = input().split()
    productlist = {}
    for i in range(1,int(moneyandcount[1])+1):
        productlist[i] = input().split()
    maindict = {}
    sidedict = {}
    for key,value in  productlist.items():
        if productlist[key][2] =='0':
            maindict[key] = productlist[key]
        else:
            sidedict[key] = productlist[key]



'''
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）
'''

def calccoord():
    input_list = input().split(';')
    initial = [0,0]
    for item in input_list:
        if not 2<= len(item) <=3:
            continue

        try:
            direction = item[0]
            step = int(item[1:])
            if 0<= step <=99:
                match direction:
                    case 'A':
                        initial[0] -= step
                    case 'D':
                        initial[0] += step
                    case 'W':
                        initial[1] += step
                    case 'S':
                        initial[1] -= step
        except:
            continue
    print(initial)


'''
取列表中相差最大的两个值
'''
def calc_num():
    list = [1, 2, 4, 7, 6, 5, 8]
    result = {}
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            keys = abs(list[i] - list[j])
            result[keys] = [i, j]
    maxkey = max(result.keys())
    print(result[maxkey])


'''
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

如果符合要求输出：OK，否则输出NG

'''
def pwdcheck():
    pwd = input()
    if  len(pwd) <= 8:
        return False
    checks = [0,0,0,0]
    for item in pwd:
        if item.isupper():
            checks[0] = 1
        if item.islower():
            checks[1] = 1
        if item.isdigit():
            checks[2] = 1
        else:
            checks[3] = 1
    if sum(checks) < 3:
        return False

    for i in range(len(pwd)-2):
        if pwd[i:i+3] in pwd[i+3:]:
            return False

    return True

# while True:
#     try :
#         if pwdcheck() :
#             print ('OK')
#         else:
#             print('NG')
#     except:
#         break



'''
现在有一种密码变换算法。
九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，
把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
数字和其它的符号都不做变换。
'''
def pwdchange():
    pwd = input()
    keyboard = {'1':1,'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9,'0':0}
    pwdlist = list(pwd)
    for item in range(len(pwdlist)):
        for i in keyboard.keys():
            try:
                if pwdlist[item] in i:
                    pwdlist[item] = str(keyboard[i])
            except:
                continue
        else:
            try:
                if pwdlist[item].isupper():
                    if pwdlist[item] == 'Z':
                        pwdlist[item] = 'a'
                    else:
                        pwdlist[item] = chr(ord(pwdlist[item].lower()) + 1)
            except:
                continue
    print(''.join(pwdlist))


'''
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。
n=0 表示输入结束，你的程序不应当处理这一行。
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
'''
def drink():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            else:
                print(n//2)
        except:
            break


'''
zhixi 在线导图收藏
结论一:gpt3.5 不行
结论二:这个接口隐藏的校验不太容易发现,走了很多弯路
'''
import requests
import json
def zhixicollect():
    liststring = """
    0c1db3f3,
    bff69860,
    17246c41,
    e316996f,
    b32de725,
    00158f08,
    eaac13eb,
    fd58ddc8,
    0b119eb0,
    b999fcb3,
    81c1fa46,
    de4df90b,
    807f3a98,
    a668df52,
    22bd58c3,
    11e2cb54,
    9aaefe08,
    67362ff4
    """

    liststring = liststring.split(',')
    for i in liststring:
        i = i.strip()
        url = "https://www.zhixi.com/api/v1/share/collect"

        payload = json.dumps({"share_id": i, "password": ""})

        headers = {
            "authority": "www.zhixi.com",
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9",
            "appid": "80001001",
            "authorization": "Bearer 1c2314d5a1fb9d63e30aada8643c40db",
            "cache-control": "no-cache",
            "content-type": "application/json;charset=UTF-8",
            "eagleeye-pappname": "b134mice77@4c48294a4d49329",
            "eagleeye-sessionid": "splvti0Ludb0RmokmpIjjq2byh9y",
            "eagleeye-traceid": "5d19721a1686644704349100949329",
            "origin": "https://www.zhixi.com",
            "pragma": "no-cache",
            "referer": f"https://www.zhixi.com/view/{i}",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.status_code, response.reason, response.text)






