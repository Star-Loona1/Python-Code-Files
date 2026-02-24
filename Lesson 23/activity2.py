'''Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary'''
numbers = [3,5,7,6,0,1]
names = ['Hana', 'Sophia', 'Roshni', 'Tejaswini']
combo = zip(numbers, names)
print(list(combo))

fruits = ['apple', 'banana', 'pear', 'mango', 'strawberry']
vegetables = ['broccoli', 'cauliflower', 'carrots', 'mushrooms']
zipped = zip(fruits, vegetables[::-1])
print(list(zipped))

furniture = ['chairs', 'tables', 'benches', 'desks', 'sofas']
stationery = ['books', 'pens', 'pencils', 'paper', 'highlighters']
dict1 = {furniture : stationery for furniture, stationery in zip(furniture, stationery)}
print(dict(dict1))
