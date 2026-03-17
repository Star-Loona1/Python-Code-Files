class Words:
    def __init__(self):
        self.string = ' '
    def inpu(self):
        self.string = input('Enter a string: ')
    def reverse(self):
        reversed_string = self.string[::-1]
        print('The string in reverse is: \n', reversed_string)
ob = Words()
ob.inpu()
ob.reverse()