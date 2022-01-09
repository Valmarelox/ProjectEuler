from math import pow



exp = 0
count = 0
for base in xrange(1, 10):
    exp = 1    
    while 1:
        res = base ** exp
        size = len(str(res))
        if size == exp:
            count += 1
            print base, exp, res, size, count
        elif abs(size - exp) > 2:
            break
        exp += 1
