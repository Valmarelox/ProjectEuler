from time import time as t
def smpf(n):
    a = 2
    while a <= n:
    #for a in xrange(2, n + 1):
        if n % a == 0:
            return a
        a += 1

def S(n):
    sum = 0
    i = 2
    while i <= n:
    #for i in xrange(2, n + 1):
        sum += smpf(i)
        i += 1
    return sum
a = [True] * (10 ** 12)
start = t()
print S(10000)
print t() - start