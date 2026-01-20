def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

choice = input("Choose an operation: \n 1. Add \n 2. Subtract \n3. Multiply \n 4. Divide")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if choice == "1":
    print("The sum of ", n1, " and ", n2, " is: ", add(n1, n2))
elif choice == "2":
    print("The difference between ", n1, " and ", n2, " is: ", subtract(n1, n2))
elif choice == "3":
    print("The product of ", n1, " and ", n2, " is: ", multiply(n1, n2))
elif choice == "4":
    print("The quotient of ", n1, " and ", n2, " is: ", divide(n1, n2))
else:
    print("This is an invalid input.")