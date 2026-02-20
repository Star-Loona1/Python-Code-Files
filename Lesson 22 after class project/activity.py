set1 = {1, 3, 6, 7, 7, 4.5, 5.5, 'a'}
print('This is set 1: ', set1)
set2 = {2, 3, 4, 5, 8, 7, 5.5}
print('This is set 2: ', set2)
print('These are the unrepeated elements: ', set1.symmetric_difference(set2))
print('These are the repeated elements :', set1.intersection(set2))