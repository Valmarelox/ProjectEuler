
def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    b = 2
    for a in xrange(2, n + 1):
        while a * b <= n:
            primes[a * b] = False
            b +=1
        b = 2
    return primes

def divisors(n):
    divs = []
    for num in xrange(1, n+1):
        if(n % num == 0):
            divs.append(num)
    return divs

def func():
    primes = sieve(100000000)
    print "Got Primes"
    s = 0
    for num in xrange(2, 100000000):
        divs = divisors(num)
        isNum = True
        for d in divs:
            if(primes[d + num / d] == False):
                isNum = False
                break
        if(isNum):
            print "Cool Nomer"
            s += num
    return s

print func()