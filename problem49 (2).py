from MyModule import PrimeNum

__author__ = 'Efraim Weiss'
import itertools
primes = PrimeNum.get_primes(10**5)
primes = filter(lambda x: x >= 1000, primes)
for prime_base in primes:
    prime_base = 1487
    base_perms = list(itertools.permutations(str(prime_base)))
    base_perms = [int(''.join(x)) for x in base_perms]
    print base_perms
    count = 0
    perms_primes = []
    for perm in base_perms:
        if perm in primes:
            count += 1
            perms_primes.append(perm)
    print perms_primes
    sums = {str(sorted([x, y])):abs(x-y) for x in perms_primes for y in perms_primes}
    dif = 0
    print sums
    for sum1 in sums.values():
        if sums.values().count(sum1) == 2:
            dif = sum1
            for key in sums:
                if sums[key] == dif:
                    print key, dif
            print dif
    print 'GOT'
    #print sums
    break