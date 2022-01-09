from decimal import *
def get_low(n):
    s = str(Decimal(n).sqrt())
    return s[:101].replace('.', '')

getcontext().precision = 300
summer = lambda s: sum((int(x) for x in s))
print sum(summer(get_low(x)) for x in xrange(100) if x not in (1, 4, 9, 16, 25, 36, 49, 64, 81, 100))

