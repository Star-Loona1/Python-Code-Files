from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print('Today is ', today)
print('\nCurrent date and time is ', now)

print('Date components ', today.year, today.month, today.day)