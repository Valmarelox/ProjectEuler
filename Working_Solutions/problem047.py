primes = set()

def sieve(n):
    sievemap = [True] * n
    sievemap[0], sievemap[1] = False, False
    for a in xrange(2, n):
        if not sievemap[a]:
            continue
        b = 2
        while a * b < n:
            sievemap[a * b] = False
            b += 1
    return map(lambda (num, isPrime): num, filter(lambda (num, isPrime): isPrime, enumerate(sievemap)))


primes = sieve(1000)



def primeFactorization(n):
    factors = []
    for p in primes:
        if n % p == 0:
            n /= p
            factors.append(p)
    return factors

def distinctFactorsCount(factors):
    return len(set(factors))

def distinctCount(n):
    return distinctFactorsCount(primeFactorization(n))

def consecPrimes(start, distincts):
    for n in xrange(start, start + distincts):
        if distinctCount(n) != distincts:
            return False
    else:
        return True



start = 0
while True:
    if consecPrimes(start, 4):
        print start
        raw_input()
    start += 1
