class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #汽车行驶的里程
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}".title()
        return long_name
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else :
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

#模拟实物
class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """电动齐策的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类"""
        super().__init__(make,model,year)    #这里不能有: , super 后面要有括号
        self.battery = Battery()             #类里面使用其他的类


my_tesla = ElectricCar('tesla', 'model s', 2019);
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



