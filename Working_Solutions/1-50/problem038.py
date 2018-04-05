from itertools import permutations


current = 1
pandigital = sorted('123456789')
while 1:
    c = ''
    for n in xrange(1, 10):
       c += str(current * n)
       if len(c) == 9:
           break
    if sorted(c) == pandigital:
        print c, current
    current += 1
