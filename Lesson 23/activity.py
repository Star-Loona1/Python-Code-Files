#add two lists
numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print('Addition of two lists:')
print(list(result))

#map sq numbers
num = [1,2,3,4,5]
def sq(n):
    return n*n
squ = map(sq, num)
print(list(squ))