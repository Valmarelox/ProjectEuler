__author__ = 'Owner'
to_div = [0, 2, 3, 5, 7, 11, 13, 17]
from itertools import permutations
from time import time as t
start =t()
get_numbers_from_indexes = lambda tup, indexes : int(''.join([str(tup[index]) for index in indexes]))
pandigitals = permutations(xrange(10))
good = []
for p in pandigitals:
    bad_number = False
    for index in xrange(1,8):
        if get_numbers_from_indexes(p,xrange(index, index + 3)) % to_div[index] != 0:
            bad_number = True
    if not bad_number:
        good.append(get_numbers_from_indexes(p, xrange(10)))
print sum(good), t() - start