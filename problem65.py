__author__ = 'Efraim Weiss'
import fractions
from itertools import chain
numerator = 2
def gen():
    l = list(chain.from_iterable([(1, k, 1) for k in xrange(2, 66 + 1, 2)]))
    print l

    for a in l:
        yield a

def calc(g):
    #if len(l) == n:
    #    return 1
    n = g.next()
    try:
        return n + fractions.Fraction(1, calc(g))
    except (IndexError, StopIteration) as e:
        return n

def builder():
    return 2 + fractions.Fraction(1, calc(gen()))
numerator = builder().numerator
print sum([ord(ch) - ord('0') for ch in str(numerator)])

#print 1 + 1 / (1 + 1 / (2))
#groupForK = lambda n : (1, K,)