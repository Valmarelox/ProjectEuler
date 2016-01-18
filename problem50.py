def sieve(n):
    primes = [True] * (n + 1)
    a = 2
    #b = 2
    primes[0:2] = [False, False]
    while a * 2<= n:
        b = 2
        while a * b <= n:
            primes[a * b] = False
            b+=1
        a+=1
    return primes

def simplify(l):
    primes = []
    for index, isPrime in enumerate(l):
        if isPrime:
            primes.append(index)
    return primes

primes = simplify(sieve(10 ** 6))
sum = 0
primeSum = 0
chain = 0
primeChain = 0
print 'sieve done'
for i, prime_start in enumerate(primes):
    sum = 0
    chain = 0
    for prime_to_add in primes[i:]:
        sum += prime_to_add
        chain += 1
        if chain > primeChain and sum in primes:
            primeSum = sum
            primeChain = chain
            print primeSum, primeChain
        if sum >= 10 ** 6:
            break
    
print primeSum, primeChain