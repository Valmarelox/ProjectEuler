from itertools import product
from decimal import *
pete = sorted([sum(x) for x in product(range(1, 5), repeat=9)])
colin = sorted([sum(x) for x in product(range(1, 7), repeat=6)])
total_options = len(pete) * len(colin)
pete = {x: pete.count(x) for x in xrange(9, 37)}
colin = {x: colin.count(x) for x in xrange(6, 37)}
print 'pete: ', len(pete)
print 'colin: ', len(colin)
print total_options, (4** 9) * (6 ** 6)
counter = 0
for op_p in pete:
    for op_c in colin:
        if op_p > op_c:
            counter += pete[op_p] * colin[op_c] #sum(colin[val] for val in colin if val < op_c)
        #counter += colin.(op_p)
print counter, total_options
print round(Decimal(counter) / Decimal(total_options), 7)


