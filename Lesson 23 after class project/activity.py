number = int(input('Enter a number: '))
print('Your number is ', number)
your_list = []
for i in range(number+1):
    your_list.append(i)
print('Your list of numbers:\n', your_list)
odd_list = [x for x in range(number+1) if x%2 == 1]
print(odd_list)

fruits = ['apple', 'banana', 'cherry', 'durian', 'grapes', 'lemon', 'orange']
print('The original list: \n', fruits)
c_fruits = [y.capitalize() for y in fruits]
print('The updated list: \n', c_fruits)