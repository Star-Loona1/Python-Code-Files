'''Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple'''

tuple1 = (1, 'codingal', 4.5, True, 'car', 5.7, 10)
print(tuple1)
tuple2 = (3, 76, 20, 50, 2, 7, 69)
print(tuple2)
tuple3 = tuple2 + (9,)
print(tuple3)
tuple4 = ('P', 'E', 'O', 'P', 'L', 'E')
a = tuple4.count('E')
print(a)
tuple5 = (10, 20, 'Emma', 5.9, 'racing', True)
z = tuple5[1:5]
print(z)