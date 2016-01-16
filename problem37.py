from math import sqrt as sq
#from math import floor

def sievecount(n):
    sum = 0
    count = 0
    primes = [True] * n
    primes[1],primes[0] = [False] * 2
    for i in xrange(2, n, 1):
        if primes[i] == True:
            if i >= 10:
                if trunc(i, primes):
                    sum += i
                    count += 1
                    print i
            mul = 2
            while mul * i < n:
                primes[i * mul] = False
                mul += 1
    return sum, count, primes
def trunc(n, primes):
    number = str(n)
    if "0" in number or "2" in number or "4" in number or "6" in number or "8" in number or "5" in number:
        return False
    for i in range(len(number) - 1, 1, -1):
        print primes[int(number[0:i])], number[0:i], number
        if primes[int(number[0:i])] == False:
            return False
        #if primes[int(number[:])] != True:#right to left
           # return False

    return True


print sievecount(33)