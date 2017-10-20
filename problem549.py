from sympy.ntheory import factorint
from itertools import count
from time import time
N = 10 ** 6
#factors = [factorint(n) for n in xrange(0, N)]

def highest_fact(base, power):
    counter = 0
    for x in count(base, base):
        tmp_x = x
        while tmp_x % base == 0:
            counter += 1
            tmp_x /= base
        #counter += factorint(x, limit=base)[base]
        if power <= counter:
            return x
def s(n):
    factors = factorint(n)
    return max(highest_fact(base, factors[base]) for base in factors)

def S(n):
    s_sum = 0
    curr_n = 2
    while curr_n <= n:
        s_sum += s(curr_n)
        curr_n += 1
    return s_sum

def old_S(n):
    return reduce(lambda sum, n: sum + s(n), xrange(2, n + 1), 0)

def test1():
    print old_S(100)

def test2():
    print S(N)

def measure(f):
    start = time()
    f()
    print time() - start

measure(test2)

