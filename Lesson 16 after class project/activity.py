try:
    age = int(input('Enter your age: '))
    if(age<18):
        raise ValueError
    else:
        print('The age is valid.')

except ValueError:
    print('The age is not valid.')
finally:
    if(age%2 == 0):
        print(age,' is an even number')
    else:
        print(age, ' is an odd number.')