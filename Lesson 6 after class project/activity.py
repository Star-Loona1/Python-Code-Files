a = input("Enter a character: ")
b = a.isalpha()

if b == True:
    print(a, " is an alphabet.")
else:
    c = a.isnumeric()
    if c == True:
        print(a, " is a number.")
    else:
        d = a.isalnum()
        if d == True:
            print(a, " is not a symbol.")
        else:
            print(a, " is a symbol.")
