
def testPrime(n):
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primeList = []

def isPrime(n):
    if n < 2:
        return False
    elif n in primeList:
        return True
    else:
        ret = testPrime(n)
        if ret:
            primeList.append(n)
        return ret

def isLeftTruncPrime(n):
    sN = str(n)
    for i, _ in enumerate(sN):
        trunc = sN[i:]
        if not isPrime(int(trunc)):
            return False
    return True

def isRightTruncPrime(n):
    sN = str(n)
    for i in xrange(1, len(sN)):
        trunc = sN[:i]
        if not isPrime(int(trunc)):
            return False
    return True

def isTruncPrime(n):
    if n < 10:
        return False
    else:
        return isLeftTruncPrime(n) and isRightTruncPrime(n)

count = 0
n = 10
l = []
#print isTruncPrime(13)
#exit(0)
while count < 11:
    if n % 20000 == 0:
        print 'mark:', n
    if isTruncPrime(n):
        print n
        l.append(n)
        count += 1
    n += 1

print sum(l)
