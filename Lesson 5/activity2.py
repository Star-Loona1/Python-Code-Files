Cost_price = float(input('Enter The Actual Product Price: '))
Selling_price = float(input('Enter The Sales Price: '))
if(Selling_price > Cost_price):
    amount = Selling_price - Cost_price
    print('Total Profit = ', amount)
else:
    print('You have no profit but A LOSS!!!')