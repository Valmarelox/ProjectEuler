from itertools import permutations

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1]  = False
    for i in range(2, n + 1):
        print i
        b = 2
        while(i * b <= n):
            primes[i * b] = False
            b+=1
    return primes

def gen(n):
    string = ""
    for a in range(1, n + 1):
        string += str(a)
    return permutations(string)

def isPrime(num):
    for a in range(3, num // 2):
        if num % a == 0:
            return False
    return True

def run():
    bigpanprime = 0
    for n in xrange(1, 987654322):
        ops = gen(n)
        for num in ops:
            num = ''.join(list(num))
            if(num[-1] == '8' or num[-1] == '6' or num[-1] == '4' or num[-1] == '2' or num[-1] == '0' or num[-1] == '5'):
                continue
            else:
                if isPrime(int(num)) and bigpanprime < int(num):
                    bigpanprime = int(num)
                    print bigpanprime

run()

