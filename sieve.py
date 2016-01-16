import time
def sieve(n):
    list = [True] * n
    b = 2
    for a in range(2, n + 1):
        if(a != False):
            b = 2
            while b * a - 2< n:
                list[b * a - 2] = False
                #print a, b, list[b*a - 2]
                b+=1
    return list

start = time.time()
n = 2000000
primes = sieve(2000000)
primesum = 0
for a in range(0, n):
    if primes[a] == True:
        #print (a + 2)
        primesum += (a +2)
print primesum, time.time() - start
