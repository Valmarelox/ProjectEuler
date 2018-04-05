def rem(a, n):
    sqr = pow(a, 2)
    return (pow(a - 1, n, sqr) + pow(a + 1, n, sqr)) % sqr

def r_max(a):
    s = set()
    for n in xrange(1, 10000):
        s.add(rem(a, n))
    return max(s)

def r_max_smart(a):
    return a ** 2 - (a if a & 1 == 1 else 2 * a)

print sum(r_max_smart(a) for a in xrange(3, 1001))
print sum(r_max(a) for a in xrange(3, 1001))
