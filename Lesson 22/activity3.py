import array as arr
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
count = 0
for i in array_num:
    if(i == 3):
        count +=1
print('Number 3 appeared ', count, ' times.')

array_num.reverse()
print('Reverse the order of the items: ')
print(str(array_num))