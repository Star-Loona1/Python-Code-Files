try:
    number = int(input('Enter a number: '))
    print("The number entered: ", number)
except:
    print("ValueError: variable number has an input of alphabet instead of numbers.")
finally:
    print('The value should be a number.')