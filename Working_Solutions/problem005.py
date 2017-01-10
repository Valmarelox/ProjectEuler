from primegen import *
HIGH = 20
primes = list(primegen(HIGH))
factors = [primefactorization(number) for number in xrange(2, HIGH)]
counts = map(lambda factor: {prime: factor.count(prime) for prime in factor}, factors)
highestperPrime = lambda prime, counts: max(factor[prime] for factor in counts if prime in factor)
print reduce(lambda a,b: a*b, [prime ** highestperPrime(prime, counts) for prime in primes])

