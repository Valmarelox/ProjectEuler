import fractions

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

min_n = 0
min_ratio = 1000
for n in xrange(2, 10 ** 7 + 1):
    phi_n = phi(n)
    if(sorted(str(phi_n)) == sorted(str(n))):
        print n
        ratio = n / phi_n
        if(ratio < min_ratio):
            min_ratio = ratio
            min_n = n


print min_n, min_ratio
