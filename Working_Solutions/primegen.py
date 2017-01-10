from itertools import count
primes = set()
def primegen(upper_limit=None):
    gen = xrange(2, upper_limit + 1) if upper_limit != None else count(2)
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

def primefactorization(n):
    factors = []
    for prime in primegen(n + 1):
        while n % prime == 0 and n != 1:
            n /= prime
            factors.append(prime)
        if n == 1:
            break
    return factors
