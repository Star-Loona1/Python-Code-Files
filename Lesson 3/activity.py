#I'm doing data types first
z = 2
print(type(z))
y = 9.22
print(type(y))
x = True
print(type(x))
w = 'Me'
print(type(w))

#Now I'm doing typecasting
#int to float
print('The data type of z before typecasting: ', type(z))
a = float(z)
print('The data type of z after typecasting: ', type(a))
#str to int
b = '67'
print('The data type of b before typecasting: ', type(b))
d = int(b)
print('The data type of b after typecasting: ', type(d))

name = input('Enter your name: ')
print('Good Morning, ', name)