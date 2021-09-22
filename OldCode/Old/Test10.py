class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.modele = model
        self.year = year
        self.odmeter = 123
        self.gas = 40

    def get_descriptive_name(self):
        long_name = str(self.year) +  ' ' + self.make + ' ' +  self.modele
        return long_name.title()

    def read_odmeter(self):
        print('This car has '+ str(self.odmeter)+ ' miles')

    def add_mile(self,miless):
        self.odmeter += miless

    def update_odmeter(self,mile):
        if mile > self.odmeter:
            self.odmeter = mile
        else:
            print('You can not update the miles!')

    def gas_tank(self):
        print('This car has '+ str(self.gas) + ' tank')

# my_new_car = Car('audi','A4','2019')
#
# print(my_new_car.get_descriptive_name())
#
# my_new_car.add_mile(11)
# my_new_car.read_odmeter()
# my_new_car.gas_tank()


class ElectCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def showbat(self):
        print('This car has '+ str(self.battery) + ' battery')

    def gas_tank(self):
        print('This car has not gas tank')


class Battery():
    def __init__(self,batt_size=70):
        self.batt_size = batt_size

    def describe_batt(self):
        print('This car has '+ str(self.batt_size) + ' battery')

my_tesla = ElectCar('telsa','X','2019')
# print(my_tesla.get_descriptive_name())
# print(my_tesla.battery)
# my_tesla.showbat()
# my_tesla.gas_tank()
my_tesla.battery.describe_batt()