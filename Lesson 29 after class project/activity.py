class BMW:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
    def disp(self):
        print('My name is: ', self.name)
        print('I am: ', self.origin)

class Ferrari():
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
    def display(self):
        print('My name is: ', self.name)
        print('I am: ', self.origin)

obj1 = BMW('BMW', 'German')
obj2 = Ferrari('Ferrari', 'Italian')
obj1.disp()
obj2.display()