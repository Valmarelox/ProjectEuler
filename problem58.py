from itertools import count, izip
from sympy import sieve
inc = 0
def spiral_gen():
    global inc
    n = 1
    for inc in count(2, 2):
        yield (n + inc, n + inc * 2, n + inc * 3, n + inc * 4)
        n += inc * 4

primes_count = 0.0
total_count = 0
try:
    for corners, total_count in izip(spiral_gen(), count(5, 4)):
        primes_count += sum(1 for x in corners if x in sieve)
        if primes_count / total_count <= 0.1:
            print total_count, primes_count, inc
except KeyboardInterrupt:
    print
    print 'total, primes, increment', total_count, primes_count, inc
    print 'Ratio:', primes_count / total_count
