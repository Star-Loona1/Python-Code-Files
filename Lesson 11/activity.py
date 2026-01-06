print('Half Pyramid Pattern of stars (*)')
r = int(input('Enter the number of rows: '))
for r1 in range(r):
    for c in range(r1+1):
        print("*", end=' ')
    print()