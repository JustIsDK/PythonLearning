class A:
    def __init__(self):
        self.name = 'xiaoming'


class B(A):
    def __init__(self):#继承A之后复写A的构造器
        super(B,self).__init__()#继承A的构造器,如果没有这句,也就没有了B.name的方法
        self.token = '1212121212'
        self.name = 'xiaowang'#继承后重写了父类的方法

class C:
    def  __init__(self,token='123456'):
        self.name = 'CCCCCCC'
        self.token = token
        
class D(C):
    def __init__(self,token='123456'):
        super(D, self).__init__(token)
        self.baseurl = 'http://www.wx.com'

if __name__ == '__main__':
    # b = B()
    # print(b.name)
    # print(b.token)
    d = D()
    print(d.token)
    print(d.baseurl)