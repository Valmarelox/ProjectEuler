from itertools import count
primes = set()
def primegen(upper_limit=None):
    start = 2 if len(primes) == 0 else max(primes) + 1
    gen = xrange(start, upper_limit + 1) if upper_limit != None else count(start)
    for prime in primes: yield prime

    for number in gen:
        if number in primes:
            yield number
            continue
        for prime in primes:               
            if number % prime == 0:       
                break
        else:
            primes.add(number)
            yield number

def isPrime(number):
    return number in primes

def primefactorization(n):
    factors = []
    for prime in primegen(n + 1):
        while n % prime == 0 and n != 1:
            n /= prime
            factors.append(prime)
        if n == 1:
            break
    return factors
