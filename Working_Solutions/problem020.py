from math import factorial

a = factorial(100)
b = 0
while a > 1:
    b += a % 10
    a /= 10
print b