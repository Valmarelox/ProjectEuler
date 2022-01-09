import time

def sieve(n):
    list = [True] * n
    b = 2
    for a in range(2, n + 1):
        if(a != False):
            b = 2
            while b * a - 2< n:
                list[b * a - 2] = False
                b+=1
    return list

def primes(list):
    prime = []
    for a, isPrime in enumerate(list):
        if isPrime == True:
            prime.append(a + 2)
    return prime

def variations(prime):
    count = 2 #starting from 2 cause skipping 2 and 5
    print "Counting"
    for a in prime:
        number = str(a)
        if ("0" in number or "2" in number or "4" in number or "6" in number or "8" in number or "5" in number):
            continue
        iscirc = 1
        for i in range(0, len(number)):
            rotate = number[i:len(number)] + number[0:i]
            if int(rotate) not in prime:
                iscirc = 0
                break
        if iscirc == 1:
            count +=1
    return count

start = time.time()
print variations(primes(sieve(1000000))), time.time() - start