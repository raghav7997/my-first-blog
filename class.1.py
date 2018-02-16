

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        name = self.make + ' ' + self.model + ' ' + str(self.year)
        return(name.title())

##my_car = Car('swift','dzire',2015)
##print(my_car.get_descriptive_name())
class ElectricCar(Car):
    def __init__(self,make,model,year,color):
        self.color = color
        super().__init__(make,model,year)


my_car = ElectricCar('Tesla','z series',2015,'white')
print(my_car.get_descriptive_name())
print(my_car.color)
