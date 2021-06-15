# l = [1,2,3,4,5]
# print(l)
# l.append(6)
# print(l)
# l.pop()
# print(l)
# l.remove(4)
# print(l)
# l[0] = 111
# print(l)
# # l.clear()
# # print(l)
# l.reverse()
# print(l)
#
# t ="a",
# print(type(t))

# a = {x:x**2 for x in (2,4,6)}
# print(a)
#
# b = a[4]
# print(b)
#

# pw = "1111"
# er = 0
# for i in range(3):
#     sr = input("请输入密码:")
#     if sr == pw:
#         print("输入正确解锁成功")
#         break
#     else:
#         if er < 2:
#             print("输入错误")
#             er = er + 1
#         else:
#             print("60s后再试")

# while TRUE:
#
#     for i in range[10, 3, 4, 7, 9, 10, 23, 12, 11, 2, 31, 23, 25, 32, 12, 11, 31]
#     if i>8:
#         print(i)

# import collections
#
# a = [1,1,1,13,3,4,5,6,6,6,6,5,5,5,4,4,4,4]
# b = collections.Counter(a)
# print(b)
# print(b.keys())
# print(b.values())



# b=[]
# for i in a:
#     b.append(a.count(i))
# b = list(set(b))
# b.sort(reverse=True)
#
# num1 = []
# for m in b:
#     for n in a:
#         if m == a.count(n):
#             num1.append(n)
#
# num2 = []
# for i in num1:
#     if i not in num2:
#         num2.append(i)
#
# print(num2)


def f(a,l=[]):
    l.append(a)
    return l
    print(l)

print(f(1))
print(f(2))
print(f(3))