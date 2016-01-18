from time import time as t
def pericheck():
    highcount = 0
    highnum = 0
    for p in xrange(12, 1000):
        count = 0
        for a in xrange(1, p/2):
            for b in xrange(a, p - a):
                if a + b >= p:
                    break
                c = p - a - b
                if a ** 2 + b**2 == c ** 2:
                    count += 1
        if count > highcount:
            print p, count
            highcount = count
            highnum = p
    return highnum, highcount

start = t()
print pericheck(), t() - start