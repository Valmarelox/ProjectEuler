from utils.primegen import primegen, isPrime

def diagonalgen(size=None):
    a = 1
    diff = 0
    while True:
        yield ((a, a + diff, a + 2 * diff, a + 3 * diff), diff)
        a += 3 * diff
        diff += 2
        a += diff
        '''a += diff
        yield a, diff - 1
        a += diff
        yield a, diff - 1
        a += diff
        yield a, diff - 1
        diff += 2
        a += diff'''
        if diff - 1 == size:
            break

print list(primegen(10))
print list(primegen(30))

diagocount = 1
primeCount = 0
for diagonals in diagonalgen():
    list(primegen(diagonals[0][-1]))
    primes = map(isPrime, diagonals[0])
    primeCount += primes.count(True)
    ratio = primeCount * 1.0 / diagocount
    print diagonals[0][-1], ratio
    if 0 < ratio <= 0.1:
        print diagonals[-1] + 1
        break
    diagocount += 4 

