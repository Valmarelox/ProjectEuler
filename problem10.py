import time
def prime(n):
    for a in range(2, n//2, 1):
        if(n % a == 0): return 0
    return 1

start = time.time()
primesum = 0
for n in range(1, 2000000, 1):
    if prime(n):
        #print n
        primesum += n
print "aA",primesum, time() - start
