__author__ = 'Owner'
from itertools import permutations
is_good = lambda a, b, c : ''.join(sorted(str(c) + str(a) + str(b))) == '123456789'
a = 1
b = 1
s = 0
to_include = []
#print ''.join(sorted(str(a * b) + str(a) + str(b)))
while a < 10000:
    b = 1
    while b < 1000:
        #print ''.join(sorted(str(a * b) + str(a) + str(b)))
        #print a, b
        c = a * b
        if is_good(a, b, c) and c not in to_include:
            s += a * b
            to_include.append(c)
            print a, b, a * b
        b += 1
    a += 1
print s
print to_include