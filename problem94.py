#!/usr/bin/env python
from math import sqrt
from time import time
P = lambda a, b, c: a + b + c
A = lambda a, b, c: sqrt(P(a, b, c) * (b + c) * (a + c) * (a + b))
p_sum = 0
start = time()
for a in xrange(0, int((10 ** 9) * 0.4)):
    if P(a, a, a -1) > 10 ** 9:
        break
    if A(a, a, a + 1).is_integer():
        p_sum += P(a, a, a + 1)
    if A(a, a, a - 1).is_integer():
        p_sum += P(a, a, a - 1)
        print a

print "Done in {time}: {sum}".format(sum=p_sum, time=(time() - start))
