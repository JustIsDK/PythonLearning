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
for i in  range(5):
    print(i)


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

s =''
a = s.split('、')
man = 0
for i in a:
    man+=1
print(man)