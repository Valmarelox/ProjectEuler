from sympy import sieve
from fractions import Fraction
MAX_D = 10 ** 6
sieve.extend(MAX_D)
closest = 0
NEXT_TO = 3 * 1.0 / 7
frac = (1,2)
for d in xrange(MAX_D, 0, -1):
    for n in xrange(1, d):
        val = n * 1.0 / d
        if val < NEXT_TO:
            if val > closest:
                closest = val
                frac = (n, d)
                print frac, closest
        else:
            break
