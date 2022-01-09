from sympy import sieve
from time import time
import sys
TARGET = int(sys.argv[1]) if len(sys.argv) == 2 else 10 ** 8
start = time()

primes = [i for i in sieve.primerange(1, TARGET / 2 + 1)]
print len(primes), time() - start

composites = set()
primes_length = len(primes)
pivot = primes_length / 2
count = 0
p = 0
try:
    for prime_index, p in enumerate(primes):
        highest_prime_to_use = TARGET / p
        iterator = reversed(primes) if prime_index < pivot else primes
        generator = ((i,x) for (i,x) in enumerate(iterator) if x < highest_prime_to_use and x >= p)
        index, x = None, None
        for index, x in generator:
            composites.add(p * x)
        if index == None:
            continue
        #print index - prime_index
        count += (index - prime_index)
except KeyboardInterrupt:
    print 'interrupted', p
print count, time() - start 
print 'res', len(composites)

