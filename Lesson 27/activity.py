'''Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.'''
class Vehicle:
    def __init__(self, name, maximum_speed, mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage
    
class Bus(Vehicle):
    def __init__(self, name, maximum_speed, mileage):
        Vehicle.__init__(self ,name, maximum_speed, mileage)
    def display(self):
        print('The name of the vehicle is ', self.name)
        print('The maximum speed is ', self.maximum_speed)
        print('The mileage is ', self.mileage)
ih = Bus('School Volvo', 180, 15)
ih.display()
