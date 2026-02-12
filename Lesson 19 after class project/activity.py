sq_lst = []
start = int(input('Enter the start point: '))
end = int(input('Enter the end point: '))
lst = []
even_lst = []
odd_lst = []
for i in range(start, end):
    a = i
    lst.append(a)
    mult = i*i
    sq_lst.append(mult)
    
for j in sq_lst:
    if j%2 == 0:
        d = j
        even_lst.append(d)
    else:
        g = j
        odd_lst.append(g)
print('The numbers between ', start, ' and ', end, ': \n', lst)
print('The square numbers between ', start, ' and ', end, ': \n', sq_lst)
print('The even square numbers: \n', even_lst)
print('The odd square numbers: \n', odd_lst)