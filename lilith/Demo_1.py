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

fib(100)
fib2(100)
