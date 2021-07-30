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

class ElectricCar(Car):
    """电动齐策的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类"""
        super().__init__(make,model,year)    #这里不能有: , super 后面要有括号
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
    #重写父类的方法,假设下面的方法父类里面有,我们要保留从父类那里继承下来的方法,丢弃不好的东西
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car does't need a gas tank!")


my_tesla = ElectricCar("tesla","model's",2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.fill_gas_tank()





