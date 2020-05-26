class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print (self.name.title()+ ' is sitting')

    def roll(self):
        print (self.name.title()+' is rolling over!')

my_dog = Dog('jay', 6)

my_dog.sit()
my_dog.roll()