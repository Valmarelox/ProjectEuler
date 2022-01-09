from sieve import sieve
from math import sqrt
primes = sieve(10 ** 6)


def calcB(a, n):
    return sqrt((n - a) / 2)

def satisfyConjecture(n):
    for p in primes:
        if p >= n:
            break
        if calcB(p, n).is_integer():
            return True
    else:
        return False


def isComposite(n):
    return n not in primes


n = 9
while True:
    if isComposite(n) and not satisfyConjecture(n):
        print "found", n
        raw_input()
    n += 2

