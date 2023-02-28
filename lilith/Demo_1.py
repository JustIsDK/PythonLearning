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

