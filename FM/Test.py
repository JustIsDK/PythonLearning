class animal:
    def eat(self):
        print('aaa')

class dog(animal):
    def eat(self):
        print('dog')


def fun(obj):
    obj.eat()


fun(dog())