class fruit :
    fruit_name = 'Apple' #class variable

    def __init__(self, color, taste): #constructor - default method
        print('This is a default constructor')
        self.color = color
        self.taste = taste
    
    def display(self): #method
        print('The color of fruit is', self.color)
        print('It tastes ', self.taste)

f1 = fruit('red', 'good')
f1.display()
