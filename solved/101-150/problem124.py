#!/usr/bin/env python3.9
from tqdm import tqdm
from sympy import sieve
from functools import reduce
from operator import mul

N = 100000 + 1

sieve.extend(N)

def divisors(n):
    for i in sieve._list:
        if n % i == 0:
            yield i

rad_couples = []

for n in tqdm(range(1, N)):
    rad_couples.append((reduce(mul, divisors(n), 1), n))

rad_couples.sort()

print(rad_couples)
print(rad_couples[4-1])
print(rad_couples[6-1])
print(rad_couples[10000-1])
