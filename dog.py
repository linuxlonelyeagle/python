class Dog:

    def __init__(self,name,age):
        #初始化
        self.name = name
        self.age  = age

    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def row_over(self):
        print(f"{self.name} rolled over!")

def main():
    my_dog = Dog("Willie",6)
    print(f"My dog's name is {my_dog.name}")
    print(f"My_dog's age is {my_dog.age}")
    my_dog.row_over()
    my_dog.sit()

main()
