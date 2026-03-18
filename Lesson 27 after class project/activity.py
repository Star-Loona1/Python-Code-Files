class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def display(self):
        self.total = self.seating_capacity*100
        self.maintain = self.total * 10 / 100
        self.final = self.total + self.maintain
        print('The number of people: ', self.seating_capacity)
        print('The total fare: ', self.total)
        print('The maintenance fee: ', self.maintain)
        print('The final fare: ', self.final)
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        Vehicle.__init__(self, seating_capacity)
    def display(self):
        Vehicle.display(self)
obj = Bus(50)
obj.display()