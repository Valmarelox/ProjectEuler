from time import time
UPPER_BOUND = 10 ** 7
expr = lambda a, n: pow(a, 2, n)

last_highest = 0
start = time()

def M_test(n):
    s = 0
    last = 0
    try:
        for a in xrange(0, n, 1):
            s += last
            print last, a, pow(a, 2, n)
            if a == pow(a, 2, n):
                last = a
    except:
        print 'Aborted at:', last
    return s

            


def M(n):
    try:
        global last_highest
        for a in xrange(n, last_highest, -1):
            #print last_highest, a
            if a == pow(a, 2, n):
                last_highest = a
                return last_highest
        return last_highest
    except:
        print
        print "Aborted at:", n, last_highest, time() - start
        raise
print M_test(10)
print time() - start
print sum(M(n) for n in xrange(1, UPPER_BOUND))
print time() - start
