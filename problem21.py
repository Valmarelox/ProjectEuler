
def d(n):
    s = 0
    for x in xrange(1, n):
        if n % x == 0:
            #print x
            s += x
    return s

def ami(upper):
    s = 0
    for n in xrange(2, upper):
        dn = d(n)
        if d(dn) == n and dn != n:
            s += n
    return s

#$print d(284)
print ami(10000)
