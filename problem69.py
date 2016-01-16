import fractions
from time import time as t

#Answer is 510510

def phi_(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

def factors(n):
    fact = []
    curr_factor = 2
    while n != 1:
        count = 0
        while n % curr_factor == 0:
            n /= curr_factor
            count += 1
        if count != 0:
            fact.append((curr_factor, count))
        curr_factor += 1
    return fact

def phi(n):
    facts = factors(n)
    curr_phi = 1
    for fact in facts:
        curr_phi *= ((fact[0] - 1) * (fact[0] ** (fact[1] - 1)))
    return curr_phi


max_ph = 0
max_n = 0
for n in xrange(2, 1000000 + 1):
    curr = n * 1.00 / phi(n)
    if curr > max_ph:
        max_ph = curr
        max_n = n
        print n, curr
print "final", max_n, max_ph