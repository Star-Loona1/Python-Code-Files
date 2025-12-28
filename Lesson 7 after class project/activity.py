'''Write a program to check the age entered by the user is between 10 to 20 years or not?'''
age = int(input("Enter your age: "))
if age < 10:
    print("You can't enroll in his class because you are ", age, "years old.")
else:
    if age <= 20:
        print("You can enroll in his class.")
    else:
        print("You can't enroll in his class.")