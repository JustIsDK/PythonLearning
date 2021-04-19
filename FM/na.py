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
#

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

'''