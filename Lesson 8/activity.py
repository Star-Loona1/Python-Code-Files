n = int(input("Enter the number whose sum you would like to find out: "))
sum = 0

for i in range(1, n+1):
    print("Sum of ", sum, " and ", i, " = ")
    sum = sum + i
    print(sum)