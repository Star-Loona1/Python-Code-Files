number = int(input('Enter a number: '))
count = 0
if number == 0:
    count = count + 1
    print(count, ' digit')

while number != 0:
     number //= 10
     count += 1
print("Number of digits: ", count)