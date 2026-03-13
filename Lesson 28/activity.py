'''Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.'''

class myClass:
    __privateVar = 29

    def __privMeth(self):
        print('Hey, how are you doing!')
    
    def hello(self):
        print('The private Variable is: ', myClass.__privateVar)

let1 = myClass()
let1.hello()
let1.__privMeth()