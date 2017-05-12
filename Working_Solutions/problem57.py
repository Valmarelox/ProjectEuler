from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import count
from math import log, floor

UPPER_BOUND = 1000

def calc(fun, n):
    temp = Fraction('0.0')
    for ni in xrange(n + 1, 0, -1):
        a, b = fun(ni)
        temp = Fraction(b) / Fraction(a + temp)
    return fun(0)[0] + temp

def fsqrt2(n):
    return (2 if n > 0 else 1, 1)


def converge2(n):
    return calc(fsqrt2, n)

def converge2_gen(n):
    num, den = 2, 1
    for _ in xrange(n):
        yield num + den, num
        num, den = 2 * num + den, num
getcontext().prec = 30
counter = 0
for two_converge in converge2_gen(1000):
    numerator, denominator = two_converge
    numer = floor(log(numerator, 10))
    deno = floor(log(denominator, 10))
    if numer > deno:
        counter += 1
print counter
