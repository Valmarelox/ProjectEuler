#bad and not optimized
import time
def prime(n):
    for a in range(n//2, 1, -1):
        if(n % a == 0): return 0
    return 1

start = time.time()
n = 1
for i in range(0, 10002, 1):
    while prime(n) == 0:
        n+=1
    if(prime(n) == 1):
        n+=1
        i+=1

print n - 1, time.time() - start
