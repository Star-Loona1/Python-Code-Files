'''Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]'''

set1 = {1, 2, 5, 7, 6, 9, 3}
print(set1)

set2 = {'w', 3.4, 7, True, 'three'}
print(set2)

set3 = {1, 2, 3, 4, 3, 2}
print(set3)

list1 = [1, 2, 3, 2]
print('The data type is ', type(list1))
set4 = set(list1)
print('The data type is ', type(set4))

list2 = [0, 1, 3, 4, 5]
list2.remove(0)
print(list2)

set5 = set(list2)
print(set5)