#0-100相加，奇偶数之和
# sum = 0
# sum2 = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum = sum + i
#     else:
#         sum2 = sum2 +i
# print("这里是偶数之和"+str(sum))
# print("这里是奇数之和"+str(sum2))

#冒泡排序
# temp = 0
# a = [1,2,3,5,6,32,463,23,46,234,2354,56,567]
# n = len(a)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if a[j] > a[j+1] :
#             a[j],a[j + 1]  = a[j+1],a[j]
# print(arr)
def fab(n):
    a,b = 0,1
    for x in range(n):
        a, b = b, a + b
    print(a, b)

fab(10)