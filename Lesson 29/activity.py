from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print('Passed value: ', x)
    
    @abstractmethod
    def task(self):
        print('I am inside the absclass')

class test_class(Absclass):
    def task(self):
        print('I am inside the test class')

testing = test_class()
testing.task()
testing.print(100)