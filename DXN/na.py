#print(sum(range (1,101)))

#def bubbleSort(arr)：
#  for i in range (1,len(arr)):
#      for j in range(0,len(arr)-i):
#         if arr[j]>arr[j+1]:
#              arr[j],arr[j+1]=arr[j+1],arr[j]
#             return arr

# a=['a','d','c','d','c','f','d']
# b=[]
# for i in a:
#     if i in b:
#         pass
#     else:
#         b.append(i)
#
# print(b)




'''
python的格式缩进很重要，
这个是注释，不删也能运行
'''

# def fab(n):
#     a,b=0,1
#     for x in range (n):
#         a,b=b,a+b
#     print (a,b)

'''
如果我们更改了代码，然后是需要提交并且推送到远端仓库的
需要这么操作
首先点击右上角的  这个commit的按钮  ctrl+k  是快捷键
就会变成这个样子，现在写的就是你的提交说明，也就是改动了什么
然后点击  commit+push   push
这样就是完整的推送流程
然后这个侧窗就可以关掉，点击上面的project
OK，明白了么明白
那么自己来一遍，
然后我们在网页端就可以看到自己的提交记录
当然在这个ide上面也可以看
啥叫然后呢？就演示个推送啊，拉代码呢
这个update就是拉代码，然后因为本地和远端可能会有差异，我演示下
还特么遇到点儿问题
11111
1111111
这个就是我刚刚提交的，所以现在你的版本和远端一致了
你以后需要改就该你这个文件的，或者新建代码文件，专门给你放个路径吧
'''


'''d={'name':'xiaoming','age':'20'}

print(d)'''


"""l=[1,2,3,4,5,6]

for x in l:
    if x>3:
    print(x)"""

"""打印100以内的奇数"""
"""a=1
while a<100:
    print(a)
    a=a+2"""


"""打印 100 以内的偶数之和"""
"""sum=0
a=1
while a<101:
    sum=sum+a
    a=a+2
print(sum)
"""

# 打印成绩:60 以下不及格,60-90 及格,90 以上优秀
# num=int(input('请输入一个成绩:')) #input里面的是字符串类型,需要把他转化为int类型
# if num<60:
#     print('不及格')
# elif 60 <= num < 90:
#     print('及格')
# elif 90<=num<=100:
#     print('优秀')
# else:
#     print('输入的成绩不合法')

# if False:
#     print('False')
# else:
#     print('True')


# # 将字符串中重复的字符去掉并计算出重复字符出现的字数,
#
# s='helloworld'
# a=set(s)
# print(f'去除重复数据后值为:{a},拼接为字符串之后为:{"".join(a)}')
# for x in a:
#     print(f'{x}在字符串{s}中出现的{s.count(x)}的次数')


# range函数  生成序列
# for i in range(5):
#     print(i)


# 用 for语句计算 1-100 偶数之和
# sum=0
# for i in range(0,101,2):
#     sum=sum+i
# print(sum)

# a=sum(range(0,101,2))
# print(a)


# break中断
# a=1
# while True:
#     if a>10:
#         break
#     a=a+1
#     print(a)


# a=1
# while True:
#     break
#     print('a')

# for x in range(10):
#     print(x)
#     if x==3:
#         break

# 当在多层嵌套循环语句中使用 break 时,break只能中断当前所在循环,比如以下的 for 循环
# while True:
#     for x in range(10):
#         if x==3:
#             break
#         print('执行for...')
#     print('执行的 while...')

# while True:
#     for x in range(10):
#         print('执行for...')
#     print('执行的 while...')
#     break


# continue 跳出当前循环继续执行
# for x in range(10):
#     print('before...',x)
#     if x==3:
#         continue
#     print('after...',x)

# for x in range (3):
#     print(x)
#     if x==1:
#         break
# else:
#     print('helloworld')


# 打印 1-100 之间的质数
# for x in range(2,100):
#     for n in range (2,x):
#         if (x/2!=0):
#             break
#     else:
#         print(f'{x}为质数')


# a=[1,2,3,4,5]
# b=['a','b','c','d','e']
# c=dict(zip(b,a))
# for key,value in c.items():
#     print(key,value)

# def say_hello():   # 定义函数
#     # pass  函数执行体的占位符,没有特殊含义,只是让程序不要报错
#     print('hello world')
#
# say_hello()   #调用函数

# 返回值
# def add():
#     a=1+1
#     return a  #a有返回值
# def bcc():
#     b=1+2  # b 没有返回值
#
# c=add()
# d=bcc()
# print (c,d)

# 返回值是什么就返回什么,不会打印 print里面的值
# def a():
#     return True
#     print('helloworld')
# i=a()
# print(i)


# sum=0
# a=0
# while True:
#     sum=sum+a
#     a=a+1
#     if a>100:
#         break
# print(sum)

# 定义一个参数,计算 50-100 之和
# def sum_1_n(m,n):#定义一个参数m,n,调用函数的时候传递参数即可
#     sum=0
#     a=m
#     for i in range(1,101):
#         sum=sum+a
#         a = a + 1
#         if i>n:
#             break
#
#     print(sum)
#     return sum
# x=sum_1_n(50,100)
# y=sum_1_n(10,50)
# print(x+y)



# 输入两个数值,自动计算两个数值之间数值之和

# def sum_n_m(m,n):
#     sum=0
#     for x in range(m,n+1):
#         sum=sum+x
#     return sum
#
# a=int(input("请输入一个数字:"))
# b=int(input('请输入一个数字:'))
# if a>=b:
#     print('第一个数字不可大于第二个数字')
# else:
#
#     print(f'{a}-{b}之和:{sum_n_m(a,b)}')


# b=1,
# print(type(b))
#
# c=[1,2,3]
# print(type(c))


# 加上*可以传任意长度
# def say(*names):
#     for x in names:
#         print(x)
# a=(1,2,3)
# say(*a)


# a=1000,2432,442,567

# def avg(*nums):
#     sum=0
#     for x in nums:
#         sum=sum+x
#     print ("和为",sum)
#     print('平均值为',sum/len(nums))
#
# avg(1000,2432,442,567)

# 元组/列表/字符串可以拆包
# def a(*args):
#     for x in args:
#         print(x)
# i=1,2,3,4
# a(*i)


# def x(**kwdjd):
#     print(kwdjd,type(kwdjd))
# x()

# 求出这个班级里面的成绩之和以及平均成绩,需要打印出他们的名字以及成绩,
# 则需要设置一个字典的函数:**
# def f(**kwargs):
#     print(kwargs)
#     sum=0
#     for k,v in kwargs.items():
#         sum=sum+v
#
#     print('他们的',len(kwargs),'个人的总成绩为',sum,sep='')
#     print('他们的平均成绩为',sum/len(kwargs),sep="")
#
# d={"xiaoming":100,"xiaoli":100}
# f(**d)
#
# 传参的顺序:*arg/**kwargs
# def f(a1,*args,a2,**kwargs):
#     print('a1',a1)
#     print('args',args)
#     print('a2',a2)
#     print('kwargs',kwargs)
# f(1,2,3,4,5,a2=100,a3=34,a4=98)

# 面试题:结果为 5
# a=5
# def f(arg=a):
#     print(arg)
# i=6
# # f()
# l = []
# def f(a):
#     l.append(a)
#     return l
# # print(f(1))
# print(f(2))
# print(f(3))


# def x_y_c(x,y,z):
#     return
#
# g=lambda x,y,z:x+2*y+z
# print(g(1,2,3))


# def f():
#     return "hello world"
#
# def g(func):
#     w=func()
#     print (w)
#
# g(f)


# def f(name,age=10,*args,**kwargs):
#     if age==10:
#         print('helloworld')
# f()   #name 为必传参数

# 创建文件 data,为写入权限,并且写入 helloworld,写入后关闭文件
# 读取文本里的数据
# f=open('./data.txt',encoding='utf8')
# print(f.readlines(13))

# ATM 取钱输入密码  密码最多输入三次,输错退出
# a=input('请输入密码:')
# count=1
# while count<3:
#     if a=='8888':
#         print('输入正确')
#         break
#     else:
#         a=input(f'第{count}次输入错误,请重新输入:')
#         count=count+1
#         if count>=3:
#             print('输入次数超限')



# ATM 取款,输入三次不可再次输入,输入非数字报错
# count=1
# while count<=3:
#     try:
#         a=int(input(f'第{count}输入密码:'))
#         if a==8888:
#             print('输入正确')
#             break
#         else:
#             print('输入错误,请重试')
#             count=count+1
#     except ValueError:
#         print('输入的字符不合法,请重新输入')
#         count=count+1
#
# print('欢迎下次再来')


# try/except ValueError语句(处理异常情况,try下面是正常情况,except后面是异常情况需要执行的)

# try:
#     A=int(input('请输入数字:'))
#     print(A)
#
# except ValueError:
#     print('语法错误')


# 计算1+1,输入上限为三次
# count=1
# while True:
#     try:
#         a=int(input('1+1=:'))
#         if a==2:
#             print('恭喜')
#             break
#         else:
#             print(f'第{count}次的答案错误请重新输入')
#             count = count + 1
#         if count>3:
#             print('错误输入达到上限,不可输入')
#             break
#     except ValueError:
#         print('输入有误,请重试')

# 可以多次使用 try,另外 try 和 except必须要组合使用
# except 里面可包含多个错误值

# while True:
#     try:
#         a=1/0
#         print('++++++')
#     except (ValueError,IOError,IndexError,TypeError,ZeroDivisionError):
#         print('错了吧')
#     try:
#         b='123'[sd]
#         print('++++++')
#     except (ValueError,IOError,IndexError,TypeError,ZeroDivisionError,NameError):
#         print('重新来')
#         break



# 异常信息别名exception as e
# def add(x,y):
#     try:
#
#         return (x+y)
#
#     except Exception as e:
#         print('引发异常',e)
#         raise
#
# a1=add(1,2)
# a2=add('12','123')
# a3=add(a1,a2)

# try:
#     a=10/0
# except :
#     print('有异常')
# finally:
#     print('hahahah')


# def f():
#     raise Exception
#
# def d():
#     try:
#         if f():
#             print('yes')
#         else:
#             print('no')
#     except:
#         print('异常')
# d()
#
# '''测试新电脑'''




# b='积分:655'
# # print(len(b))
# # print(b[1])
# # print(b[-3])
# # print(b[::-1])
# # print(b[1:3:2])
# print(b[1:3:])

# 定义函数
# def sayhello():
#     print('hello world')
#
# # 函数只有在调用的时候才会执行
# sayhello()



# def sum100():
#     s = 0
#     for i in range(1,101):
#         s = s+i
#     print(s)
#
# # 调用函数
# sum100()


# n 为函数的参数，可以理解为一个变量
# def sum100(n):
#     print(f'计算1-{n}之和：',end='')
#     s = 0
#     for i in range(1,n+1):
#         s = s+i
#     print(s)
#
# # 调用函数
# sum100(100)
#
# sum100(10000)
#
# sum100(2345)


# i=0
# for i in range(1,100):
#     i=i+1
# print(i)

# class Person:
#     name = "张三" # 类变量
#     age = 20     # 类变量

# # 访问类变量
# print(Person.name)
# print(Person.age)
#
# # 实例化类
# p1 = Person() # 实例化对象赋值给 p1 变量
# print(p1.name,p1.age)
# p1.name = "xiaoming" # 更改实例化对象的属性值
# p1.age = 10
# p2 = Person()
# print(p2.name,p2.age)
# p2.name = "lisi"
# p2.age = 21
#
# print(p1.name,p1.age,p2.name,p2.age) # xiaoming 10 lisi 21

# def f(a,b,c):
#     """
#
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """

# a=1.01**3
# b=0.99**2
# print(a*b)


# price_str=input('苹果的单价:')
# weight_str=input('苹果的重量:')
#
# price=float(price_str)
# weight=float(weight_str)
# money=price*weight
# print(money)


# price_str=input('苹果的单价:')
# weight_str=input('苹果的重量:')

# price=float(input('苹果的单价:'))
# weight=float(input('苹果的重量:'))
# money=price*weight
# print(money)

# 格式化输出
# name ='大明'
# print('我的名字叫%s,请多多关照!'% name)
# student_no=1
# print('输出我的学号是%06d '%student_no)
# scale=10
# print('输出数据比例为 %0.2f%%'% scale)
# price=9
# weight=5
# money=float(price*weight)
# print('输出苹果单价%0.2f元/斤.购买了%0.2f斤,需要支付%0.2f元'%(price,weight,money))



# '''if语句'''
# age=18
#
# if age>18:
#     print('满足18岁可以去嗨皮')
#
# else:
#     print('不可以去嗨皮')

# age=int(input('请输入年龄:'))
# if age>18:
#     print('满足18岁可以去嗨皮')
# else:
#     print('不可以去嗨皮')



# '''逻辑运算  and or not'''
# age=int(input('请输入年龄:'))
# if age>=0 and age<=120:
#     print('年龄正确')
# else:
#     print('年龄不正确')


# python_score=60
# c_score=57
# if python_score >60 or c_score>60:
#     print('考试通过')
# else:
#     print('考试不通过')

# '''布尔型变量is_employee '''
# is_employee=True
# if not is_employee:
#     print('非本公司人禁止入内')
# else:
#     print('本公司员工可以入内')


# '''elif增加判断条件'''
# holiday_name='平安夜'
# if holiday_name=='情人节':
#     print('买玫瑰')
#     print('看电影')
# elif holiday_name=='平安夜':
#     print('买苹果')
#     print('吃大餐')
# elif holiday_name=='生日':
#     print('买蛋糕')
#     print('吃大餐')
# else:
#     print('每天都是节日啊')

# '''if嵌套语句'''
# has_ticket=True
# knife_length=19
# if has_ticket :
#     print('车票检查通过,准备开始安检')
#     if knife_length >20:
#         print('刀太长了,有%d厘米'%knife_length)
#         print('不允许上车')
#     else:
#         print('可以上车')
# else:
#     print('请先买票')

# '''随机数'''
# '''导入工具包 random 要放在代码前面做引入'''
# '''石头1剪刀2布3'''
# import random
# player=int(input('玩家输入的拳:'))
# computer=random.randint(1,3)
#
# print('玩家选择的拳头是%d-电脑出的拳头是%d'%(player,computer))
# if ((player==1and computer==2)
#         or (player==2and computer==3)
#         or (player==3 and computer==1)):
#      print('赢了')
# elif (player==computer):
#     print('平局')
# else:
#     print('输了')


# '''循环'''
# '''while'''
# i=0
# while i<3:
#     '''希望在循环内执行的代码'''
#     print('hello')
#     '''处理计数器'''
#     i+=1
# print('查看循环结束后i=%d'%i)


# '''计算0-100之和'''
# i=0
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(`sum)

# '''求0-100之间偶数之和'''
# i=0
# sum=0
# while i<=100:
#     '''判断数值是否为偶数'''
#     if i%2==0:
#         sum = sum + i
#     i=i+1
#
# print('0-100偶数之和为%d'%sum)
#
#
# '''求0-100之间奇数之和'''
# i=0
# sum=0
# while i<=100:
#     '''判断数值是否为偶数'''
#     if i%2!=0:
#         '''当满足if条件时,在进行累加操作'''
#         sum = sum + i
#     i=i+1
#
# print('0-100奇数之和为%d'%sum)


# '''break某一条件满足时,退出循环,不在执行后续代码'''
# '''定义一个计数变量'''
# i=0
# while i<10:
#     '''break某一条件满足时,退出循环,不在执行后续代码'''
#     '''i=3的时候  终止代码 '''
#     if i==3:
#         break
#     print(i)
#     i=i+1
#


# '''continue某一条件满足时,不执行后续重复代码'''
# '''定义一个计数变量'''
# i=0
# while i<10:
#     if i==3:
#         '''注意再循环中使用continue,需要 确认循环计数是否修改'''
#         '''否则会导致死循环'''
#         i = i + 1
#         continue
#
#     print(i)
#     '''处理逻辑'''
#     i=i+1

# '''未修改计数 会导致死循环 '''
# i=0
# while i<10:
#     if i==3:
#        '''未进行计数修改,会导致死循环'''
#         continue
#
#     print(i)
#     '''处理逻辑'''
#     i=i+1


#
# '''while嵌套'''
# '''在控制台输入五行*  每行递增'''
# '''定义一个计数器变量'''
# row=1
# while row<=5:
#     print('*'*row)
#     row+=1


# '''(不想要print函数输入过后不需要换行的时候 需要总的print里面加上end='')'''
# print('*',end='---')
# print('*')


# row=1
# while row<=5:
#     '''增加一个小的循环,专门负责当前行中,每一列的星星显示'''
#     '''定一个计数器变量'''
#     col=1
#     while col<=row:
#         print('*',end='')
#         col=col+1
#     '''这行代码的目的就是每行打印完之后换行'''
#     print('')
#     row+=1



# '''九九乘法表'''
# def ff():
#     row=1
#     while row<=9:
#         col=1
#         while col<=row:
#             print('%d*%d=%d'%(col,row,col*row),end='\t')
#             col=col+1
#
#         print('')
#         row=row+1
#
#
# ff()
#
# '''函数'''



# def xiaosun(x,z,y=2):
#     print(x+y+z)
#
# xiaosun(1,2,y=4)


