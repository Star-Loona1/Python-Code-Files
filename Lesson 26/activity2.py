'''Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!'''
class employee:
    def __init__(self):
        print('Hello, My name is Dua')
    def __del__(self):
        print('Destructor function called!')

def creating_object():
    obj = employee()
    del obj
creating_object()