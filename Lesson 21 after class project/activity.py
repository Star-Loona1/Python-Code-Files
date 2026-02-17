test_dictionary = {'If' : 3, 'racecar' : 2, 'delivery' : 4, 'jacket' : 4, 'tea' : 4, 'book' : 1, 'pen' : 3}
print(test_dictionary)
diction = int(input('Enter the value you want to check: '))
res = 0
for i in test_dictionary:
    if(test_dictionary[i] == diction):
        res = res + 1

print('Frequency is ', str(res))