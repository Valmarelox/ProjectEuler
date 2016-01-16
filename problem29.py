def distinct(lower, upper):
    l = []
    for a in xrange(lower, upper + 1):
        for b in xrange(lower, upper + 1):
            c = a ** b
            if a ** b not in l:
                l.append(c)
    return l

print len(distinct(2, 100))