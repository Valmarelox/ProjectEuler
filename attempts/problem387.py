primes = []
prime_nums = []
def sieve(n):
    global primes
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for a in xrange(2, (n + 1)):
        if primes[a] == False:
            continue
        b = 2
        while a * b <= n:
            primes[a * b] = False
            b+=1
    return primes

def digsum(n):
    digs = reduce(lambda x, y: x + int(y), str(n), 0)
    while digs > 10:
        digs = reduce(lambda x, y: x + int(y), str(digs), 0)
    return digs

def checkHarshad(n):
    global primes, prime_nums
    if n < 10:
        return True
    if n % digsum(n) == 0:
        print int(str(n)[:-1])
        return checkHarshad(int(str(n)[:-1]))
    else:
        return False
def checkPrimeHarshad(n):
    if int(n[:-1]) % digsum(int(n[:-1])) == 0:
        print 'y'
        if primes[int(n[:-1]) / digsum(int(n[:-1]))]:
            print 'p'
            return checkHarshad(int(n[:-1]))
    else:
         return False

def run(upper, prime_nums):
    s = 0
    for n in prime_nums:
        if(10000 > n > 10 and checkPrimeHarshad(str(n))):
            s +=n
    return s
sieve(100000)
prime_nums = [x[0] for x in filter(lambda x: x[1], enumerate(primes))]
print 'starting'
#print checkPrimeHarshad('2011')
print run(10000, prime_nums)