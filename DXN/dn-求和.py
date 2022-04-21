# '''求和'''
# def sum():
#     row=0
#     sum=0
#     while row<100:
#         row+=1
#         sum = sum + row
#
#     print(sum)
#
# #--------------------------------------------------------------
#
# '''
# 反转循环打印字符串”helloworld”
# '''
# def p():
#     i='helloworld'
#     print(i[::-1])
#
# #--------------------------------------------------------------
#
#
# '''
# 定义字符串line='I am a beautiful girl'，变化为：girl beautiful a am I
# '''
# def change():
#     i = ['I', 'am', 'a', 'beautiful', 'girl']
#     print(i[::-1])
#     print(type(i))
#
#
# #--------------------------------------------------------------
#
#
# '''
# 定义字典元素的列表：stds_list= [
# {"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
# {"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
# {"id": 3, "name": "小东", "c_s": 79, "python_s": 83},
# ]
# 显示学生信息：“学生id：1，学生姓名：小明，C语言成绩：85, Python成绩：78”。
# '''
# stds_list= [{"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
#             {"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
#             {"id": 3, "name": "小东", "c_s": 79, "python_s": 83}]
# def prt():
#     for i in stds_list:
#         print('学生id:' + str(i["id"]) + ',学生姓名:' + i["name"] + ',C语言成绩:' + str(i["c_s"]) + ',Python成绩:' + str(
#             i["python_s"]))
#
# # print('学生id:' + str(stds_list[0]["id"]) + ',学生姓名:' + stds_list[0]["name"] + ',C语言成绩:' + str(stds_list[0]["c_s"]) + ',Python成绩:' + str(i["python_s"]))
#
# #--------------------------------------------------------------
#
#
# '''
# 输入一行字符,统计其中有多少个单词，每两个单词之间以空格隔开。
# 如输入: This is a Python program. 输出：There are 5 words in the line
# '''
# def calc() :
#     i = str(input('请输入一行字符:'))
#     li = i.split(" ")
#     print(li)
#     n = len(li)
#     print(f'there are {n} words in the line')
#
# #--------------------------------------------------------------
# '''
# * 提示用户输入姓名
# * 然后输出 Hi + 姓名
# '''
# def a():
#     name=input('请输入姓名:')
#     print('HI'+name)
# #--------------------------------------------------------------
# '''
# ## 邮件机器人
# * 假设计你是要给自动给客户发邮件的运营人员
# * 提示运营人员输入姓名
# * 提示运营人输入购买的商品
# * 输出邮件格式如下：
#
# Dear [用户姓名]:
#
#     Your purchased product : [产品名] is delivered!
#
#     Thanks for your choosing!
#
# '''
# def f():
#     name=input('输入姓名:')
#     product=input('输入购买的商品:')
#     print(f'Dear {name}:\n'
#           f'\tYour purchased product :{product} is delivered!\n'
#           f'\tThanks for your choosing!')
#
# #--------------------------------------------------------------
#
# '''
# ## 截取字符串
# 从 "You Rise Me Up" 中截取 Rise
# '''
# def y():
#     i='You Rise Me Up'
#     li=i.split(' ')
#     print(li)
#     print(li[1])
# #--------------------------------------------------------------
#
#
# '''
# ## 字符串大小写转换
# 将 "Python Basic" 转成小写
# '''
# def xiaoxie():
#     h="Python Basic"
#     print(h.lower())
# def daxie():
#     h = "python basic"
#     print(h.upper())
#
# #--------------------------------------------------------------
#
# '''
# ## 数值计算
# * 计算 1000 乘以 2000，再减 1000000
# * 打印出结果
#
# '''
# def calc1():
#     i=1000
#     p=2000
#     c=100000
#     print(i*p-c)
#
# #--------------------------------------------------------------
# '''
# ## 变量类型 (附加题，不考)
# * 猜一下下面两行代码的执行结果：
# * print(type(100))
# * print(type("Hello"))
#
# '''
# #--------------------------------------------------------------
#
#
# '''
# 题目：
#
# * 在中国 1～3月为春季，4～6个月为夏季，7～9月为秋季，10～12月为冬季；
# * 提示用户输入一个月份（数字），然后输出是什么季节；
# * 如果用户输入 1～12 之外的数字，提示 "机器故障"。
#
#   备注：因为是学习的第二天，所以暂时让用户输入，以后可以直接读系统中的日期
#
#
# '''
# def season():
#     n=int(input('请输入月份:'))
#     if 1<=n<=3:
#         print('现在是春季')
#     elif 4<=n<=6:
#         print('现在是夏季')
#     elif 7<=n<=9:
#         print('现在是秋季')
#     elif 10<=n<=12:
#         print('现在是冬季')
#     else:
#         print('机器故障')
# #--------------------------------------------------------------
# '''
# # 3. 价格预警机器人
# * 假设你要监控  A,B,C 三个商品
# * 如果 A/B/C 分别降价 30/20/10 元上，就要报警
# * 提示用户输入商品名（A/B/C)
# * 提示用户输入降价值 (数字）
# * 如果需要报警则打印商品名 + 降价值
#
# '''
# def price():
#     base = {'A':30,'B':20,'C':10}
#     h=input('请输入商品名:').upper()
#     c=int(input('请输入降值价格:'))
#     if c > base[h]:
#         print(f'{h}  +  {str(c)}')
# #--------------------------------------------------------------
#
# '''
# ---
# 题目：
#
# * 假设你现在是考试院的老师，在看试卷，要打评语
# * 提示用户输出考试分数（数字），分数范围是0 ~ 100 分
# * 如果输入值小于 60 分，则打印 "要加油呀!"
# * 如果输入值大于等于 60 分，且小于 80分，则打印 "不错呀，认真学习了！"
# * 如果输入值大于等于 80 分，则打印 "考得不错，不要骄傲！"
# * 不在 0～100 分范围内的输入，我不需要打印任何信息
#
#   备注：因为是学习的第二天，所以暂时让用户输入，以后可以直接读取成绩表，直接出评语
#
# ---
# 解题讲解：
#
# 此题为2，3题的变体，故不再专门解释！
#
# * 特别注意的是，本题不需要使用 else
# * 在 if/elif 的组合里要考虑用户输入值不在 0~100 的情况
#
# '''
# def s():
#     score=int(input('请输入考试分数:'))
#     if score<60:
#         print('要加油呀!')
#     elif 60<=score<=80:
#         print('不错呀，认真学习了！')
#     elif 80<score<100:
#         print('考得不错，不要骄傲！')
#     else:
#         pass
# #--------------------------------------------------------------
#
# '''
# # 5. 智能空调机器人
#
# ---
# 题目：
#
# * 假设你现在设计一台智能空调
# * 提示用户输入季节（只能是 winter/summer)
# * 提示用户输入当前温度 (数字）
# * 如果季节是 winter， 且温度低于10度，则打印 "太冷了，开热空调了"
# * 如果季节是 summer， 且温度高于27度，则打印 "太热了，开冷空调了"
# * 如果是不符合上面条件的用户输入，则不用打印任何东西
#
#   备注：因为是学习的第二天，所以暂时让用户输入，以后可以接外部温度电子器直接读
#
# ---
# 解题讲解：
#
# 此题为2，3题的变体，故不再专门解释！
#
# 特别注意的是，本题不需要使用 else
#
# '''
# def ss():
#     s={'winter':10,'summer':27}
#     h=input('请输入季节:')
#     i=int(input('请输入当前温度:'))
#     if i>s[h]:
#         print('太冷了,开热空调了')
#     elif i<s[h]:
#         print('太热了，开冷空调了')
#     else:
#         pass
# #--------------------------------------------------------------
# '''
# # 2. 智能日历第一步，打印12个月
# ---
# 题目：
#
# * 你是智能日历的程序员
# * 请打印出 1～12月，每月一行
# '''
# def nn():
#     n=0
#     n=int(input('请输入月份:'))
#     while 1<=n<=12:
#         print(f'{n}月')
#         n+=1
#
# #--------------------------------------------------------------
# '''
# # 3. 用 for 循环计算1到4的连乘
# ---
# 题目解析:
#
# * 在 Python 中，乘法符号是 *
# * 最笨的办法是 1 乘 2 乘 3 乘 4
# * 但是如果要 1 ～ 10000 的连乘你就傻眼了所以我们使 for 循环
# '''
# def ss():
#     sum=1
#     for i in range(1,10000):
#         sum=sum*i
#
#     print(sum)
#
# #--------------------------------------------------------------
# '''
# # 4. 用 for 循环打印 "Good Day!" 里的每个字符
# ---
# 题目解析:
#
# * "Good Day!" 是一个字符串
# * 我们可以用 for 循环来遍历访问它
#
# ---
# '''
# def ff():
#     n='Good Day!'
#     for i in n:
#         print(i,end="")
# #--------------------------------------------------------------
# '''
# # 5. for 循环打印出所有 1~50 之间的所有偶数
# '''
#
# def aa():
#
#
#     for c in range(0,51,2):
#             print(c)
#
# #--------------------------------------------------------------
# '''
# remove删除匹配到的第一个指定元素'z',for循环开启,第一次b=i[0],匹配到'z',删除,列表为['z','z','n','z','z','w'],
# 再次进入循环b=i[1],匹配到'z',删除,列表减少一个z为['z','n','z','z','w'],一直循环到i[3],列表只剩下['n','z','w'],取不到i[3],循环结束
# '''
# def pp():
#     i=['z','z','z','n','z','z','w']
#     for b in i:
#         i.remove('z')
#     print(i)
# #--------------------------------------------------------------
# '''增加数据'''
# def nn():
#     name_list=['zhangsan','lisi','wangwu']
#     '''
#     index索引,已知值,确定值所在的列表位置
#     '''
#     n=name_list.index('zhangsan')
#     print(n)
#
#     '''修改数据'''
#     name_list[1]='xiaohong'
#     print(name_list)
#
#     '''增加数据append,可以向列表末尾增加数据'''
#     name_list.append('xiaoli')
#     print(name_list)
#     '''insert,可以在指定的索引位置插入数据'''
#     name_list.insert(1,'haha')
#     print(name_list)
#     '''extend可以吧其他列表中的完整内容追加到当前列表的末尾'''
#     temp_list=['孙悟空','猪二哥','沙师弟']
#     name_list.extend(temp_list)
#     print(name_list)
#
# #--------------------------------------------------------------
# '''删除数据'''
# '''remove方法可以从列表中删除指定的数据'''
# def  ff():
#     name_list =['zhangsan', 'haha', 'xiaohong', 'wangwu', 'xiaoli', '孙悟空', '猪二哥', '沙师弟']
#     name_list.remove('wangwu')
#     print(name_list)
#     '''pop可以删除列表中最后一个元素'''
#     name_list.pop(0)
#     '''pop可以指定要删除元素的索引'''
#     name_list.pop(-1)
#     print(name_list)
#     name_list.clear()
#     print(name_list)
#     '''del删除列表元素'''
#     name_list =['zhangsan', 'haha', 'xiaohong', 'wangwu', 'xiaoli', '孙悟空', '猪二哥', '沙师弟']
#     del name_list[3]
#     '''删除了name_list'''
#     del name_list
#     '''执行报错  因为name_list已经被删除了'''
#     print(name_list)
#
# #--------------------------------------------------------------
# '''len  长度'''
# def aaa():
#     age_list=['3','55','56','17']
#     a= len(age_list)
#     print(a)
#
#     '''count计数,统计列表中某一个数据出现的次数'''
#     age_list=['3','55','56','17','55','56']
#     b=age_list.count('55')
#     print(b)
#     #--------------------------------------------------------------
# '''升序'''
# def bbb():
#     name_list=['heihei','yoyo','wangwu','lisi','zhangsan']
#     num_list=[5,3,7,2,8,1]
#     c=name_list.sort()
#     print(name_list)
#     '''降序'''
#     name_list=['heihei','yoyo','wangwu','lisi','zhangsan']
#     c=name_list.sort(reverse=True)
#     print(name_list)
#
#     '''反转'''
#     name_list=['heihei','yoyo','wangwu','lisi','zhangsan']
#     c=name_list.reverse()
#     print(name_list)
#
# # --------------------------------------------------------------
# '''
# 题目：
#
# * 程序员把产品星级放入一个列表 [3,5,4,2,1,5,5]
# * 请把所有小于4的评分打印出来
#
#   请在 for 循环里跳过所有大于等于4星的星级（用 continue)
#
# ---
# '''
# def dfd():
#     star=[3,5,4,2,1,5,5]
#     for i in star:
#         if i<4:
#             print(i)
#
# # --------------------------------------------------------------
# '''
# # 7. 自动邮件机器人
# ---
# 题目：
#
# * 假设你是负责给客户发邮件的运营人员
# * 你现在学了 Python想开发一个发邮件机器人
# * 程序可以一直运行
#   提示运营人员输入姓名
#   提示运营人输入购买的商品
#   然后根据输入的姓名/商品名拼接输出邮件
#   输出邮件格式如下：
# Dear [用户姓名]:
#     Your purchased product : [产品名] is delivered!
#     Thanks for your choosing!
# *  使用 while 来循环提示用户输入，直到用户在姓名中输入 ! 才退出(用break)
# '''
# def yy():
#
#     name=str(input('请输入用户姓名:'))
#     pru=str(input('请输入产品名:'))
#     while True:
#         if name=='!':
#             print(f'Dear {name}:'
#                    f'Your purchased product : {pru} is delivered!'
#                     f'Thanks for your choosing!')
#         else:
#             print(
#             )
#             break
# # --------------------------------------------------------------
#
# for i in range(10,0,-1):
#     star=(2*i-1)*'*'
#     blank=(10-i)*' '
#     print(blank+star)

import copy
a=[1,2,3]
b=copy.deepcopy(a)
print(id(a))
print(id(b))

c=copy.copy(a)
print(c)
print(a)
print(id(a))
print(id(c))
