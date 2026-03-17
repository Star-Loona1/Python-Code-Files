class BMW:
    def __init__(self, name, origin, fuel_type, max_speed):
        self.name = name
        self.origin = origin
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def disp(self):
        print('My name is ', self.name)
        print('I am ', self.origin)
        print('My fuel type is ', self.fuel_type)
        print('My max speed is ', self.max_speed)

class Ferrari():
    def __init__(self, name, origin, fuel_type, max_speed):
        self.name = name
        self.origin = origin
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def display(self):
        print('My name is ', self.name)
        print('I am ', self.origin)
        print('My fuel type is ', self.fuel_type)
        print('My max speed is ', self.max_speed)

obj1 = BMW('BMW', 'German', 'Diesel', 155)
obj2 = Ferrari('Ferrari', 'Italian', 'Ethanol-free petrol', 211)
obj1.disp()
obj2.display()