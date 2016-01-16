from math import pow
a = int(pow(2, 1000))
#print a
b = 0
sum = 0
while a >= 1:
    b = a % 10
    sum += b
    a /= 10
print sum