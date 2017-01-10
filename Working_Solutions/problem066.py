__author__ = 'efraim'
from math import sqrt

def equation(d):
    if sqrt(d) ** 2 == d:
        return 0,0
    x = 0
    y = 0
    while 1:
        x +=1
        dysqrd = x ** 2 -1
        if (dysqrd % d != 0):
            continue
        y = sqrt(dysqrd / d)
        if(y != 0 and (x ** 2 - d * (int(y) ** 2) == 1)):
            break
    print "d=", d, "eq",x ** 2, "-", d, "*", int(y) ** 2, (x ** 2 - d * (int(y) ** 2) == 1)
    return x, int(y)

l = {}
for d in xrange(1,1001):
    l[d] = equation(d)[0]
print l
print max(l.values())
