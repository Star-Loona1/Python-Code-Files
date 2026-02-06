import math

print('I am using the math module \nLets do trigonometric calculations.')
number = float(input('Enter a number of your choice: '))
trig_cos = math.cos(math.radians(number))
print('The cos value of ', number, ' is ', trig_cos)
trig_sin = math.sin(math.radians(number))
print('The sin value of ', number, ' is ', trig_sin)
trig_tan = math.tan(math.radians(number))
print('The tan value of ', number, ' is ', trig_tan)