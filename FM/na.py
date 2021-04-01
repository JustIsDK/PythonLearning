#print(sum(range (1,101)))

#def bubbleSort(arr)：
#  for i in range (1,len(arr)):
#      for j in range(0,len(arr)-i):
#         if arr[j]>arr[j+1]:
#              arr[j],arr[j+1]=arr[j+1],arr[j]
#             return arr
'''
a=['a','d','c','d','c','f','d']
b=[]
for i in a:
    if i in b:
        pass
    else:
        b.append(i)

print(b)
'''

'''
python的格式缩进很重要，
这个是注释，不删也能运行
'''

def fab(n):
    a,b=0,1
    for x in range (n):
        a,b=b,a+b
    print (a,b)