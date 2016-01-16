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

def sum(n):
    isprime = sieve(n)
    primes = [x[0] for x in filter(lambda x: x[1], enumerate(isprime))]
    #print primes
    print len(primes)
   # print primes
    s = 0
    longest = [0,0]
    for i, a in enumerate(primes[::-1]):
        s = a
        print i
        count = 0
        for b in primes[::-1][i + 1::]:
            s -= b
            count += 1
        # print sum
            if(s < 0):
                break
            #print "Primes:",s, count
            if(s == 0):
                print "Found", a
                #print "found:",s, count
                if(count > longest[0]):
                    longest[0] = count
                    longest[1] = a
    print "The best", longest

sum(1000)
