from sympy import sieve, factorial

UPPER_BOUND = 10 ** 8

def S(p):
    val = 0
    k = p - 5
    factor = factorial(k)
    val = (val + factor) % p
    for k in xrange(4, 0, -1):
        factor *= (p - k)
        val = (val + factor) % p
    return val % p

def sigma_S(lower_range, upper_range):
    primes = sieve.primerange(lower_range, upper_range)
    print 'sieved primes'
    sigma = 0
    for prime in primes:
        sigma += S(prime)
    return sigma


print "S(7) =", S(7)
sig = sigma_S(5, 10 **8)
print "Sum:", sig
