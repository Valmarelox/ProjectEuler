from itertools import permutations

def sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    mul = 2
    for i in range(2, n // 2 + 1):
        if primes[i] == True:
            while i * mul < n:
                primes[i * mul] = False
                mul += 1
            mul = 2
    return primes
def check2(list):
    if list[2] - list[1] == list[1] - list[0]:
        return True



def check1(primes):
    permis = 0
    for i in range(1000, 10000):
        if primes[i] == True:
            permis = permutations(str(i))
            fit = True
            count = 0
            list = []
            permis = [int(''.join(x)) for x in permis]
            #print permis
            #
            #input()
           # print permis.next()
            for a in permis:
                if count == 3:
                    break
                elif primes[int(a)] == True:
                    list.append(a)
                    count += 1
            if count == 3:
                if check2(list):
                    print list
                    #return
def check(primes):
    for i in range(1000, 10000):
        digits = []
        for a in str(i):
            digits.append(a)
        for j in range(i + 1, 10000):
            fail = 0
            list =[]
            for dig in digits:
                #print j
                if dig not in str(j):
                    fail = 1
                    break
            if fail == 0:
                if primes[j] == True:
                    list.append(j)
                    print j
            if len(list) == 3
primes = sieve(10000)
check(primes)
#check1(primes)
