'''Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.'''

attendance = int(input("Enter your attendance: "))
if (attendance > 75):
    print("You are allowed for the examination")
else:
    answer = input("Do you have a medical cause? \nEnter Y for yes or N for no")
    if (answer == 'Y'):
        print("You are allowed to the examination with medical cause")
    else:
        print("You are not allowed")