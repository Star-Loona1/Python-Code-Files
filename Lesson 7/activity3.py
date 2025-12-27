'''Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user for better selection options.'''

print("Select your ride: ")
print("1. Bike")
print("2. Cars")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("Select your bike: ")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice2 = int(input("Enter your bike choice: "))
    if choice2 == 1:
        print("You have selected scooty.")
    elif choice2 == 2:
        print("You have selected scooter.")
    else:
        print("This is not among the selections provided, try using the given selections provided.")

elif choice == 2:
    print("Select your car: ")
    print("1. Sedan")
    print("2. XUV")
    print("3. Mercedes Benz")
    print("4. Lamborghini")
    choice3 = int(input("Enter your car choice: "))
    if choice3 == 1:
        print("You have selected sedan.")
    elif choice3 == 2:
        print("You have selected XUV.")
    elif choice3 == 3:
        print("You have selected mercedes benz.")
    elif choice3 == 4:
        print("You have selected lamborghini.")
    else:
        print("This is not among the selections provided, try using the given selections provided.")

else:
    print("Wrong choice.")