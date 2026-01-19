decimal_number = float(input("Enter a decimal number: "))
base = 2

if decimal_number == 0:
    print('0')

binary_result = ""
temp_num = decimal_number

while temp_num > 0:
    remainder = temp_num % 2
    binary_result = str(int(remainder)) + binary_result
    temp_num = temp_num // 2

print(binary_result)