from math import pow
from time import time

primeList = []

def testPrime(n):
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isPrime(n):
    if n < 2:
        return False
    if n in primeList:
        return True
    else:
        ret = testPrime(n)
        if ret:
            primeList.append(n)
        return ret


def iterateOnPrimes(a, b):
    n = 0
    while isPrime(pow(n, 2) + a * n + b):
        n += 1
    return n


print iterateOnPrimes(-79, 1601)
exit(0)

start = time()
heighestChain = 0
coeffecients = ()
for a in xrange(-999, 1000):
    for b in xrange(-1000, 1001):
        count = iterateOnPrimes(a, b)
        if count > heighestChain:
            heighestChain = count
            coeffecients = (a, b)

print heighestChain, coeffecients, coeffecients[0] * coeffecients[1]
print time() - start
