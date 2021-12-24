from math import sqrt
a = float(input('Enter the first side '))
b = float(input('Enter the second side '))
c = float(input('Enter the third side '))

if a+b < c or a + c < b or b + c < a:
    print('This triangel doesnt exist')
else:
    p = (a + b + c)/2
    s = sqrt(p * (p-a) * (p-b) * (p-c))
    print(s)