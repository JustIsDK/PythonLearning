class A:
    def __init__(self):
        self.name = 'xiaoming'


class B(A):
    def __init__(self):#继承A之后复写A的构造器
        super(B,self).__init__()#继承A的构造器,如果没有这句,也就没有了B.name的方法
        self.token = '1212121212'
        self.name = 'xiaowang'#继承后重写了父类的方法

if __name__ == '__main__':
    b = B()
    print(b.name)
    print(b.token)