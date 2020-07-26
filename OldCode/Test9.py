class Res():

    def __init__(self,name,type):
        self.name =  name
        self.type = type

    def des(self):
        print('这个餐厅的名字是： '+ self.name.title())

    def open(self):
        print('餐厅正在营业呀')


res = Res('天府汇','China')

res.des()
res.open()