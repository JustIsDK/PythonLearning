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
for x in range(2,100):
    for n in range (2,x):
        if (x/2!=0):
            break
    else:
        print(f'{x}为质数')