

isPali = lambda n: int(str(n)[::-1]) == n

def islychrel(n):
    for iteration in xrange(50):
        n = n + int(str(n)[::-1])
        if isPali(n):
            return False
    else:
        return True


print len(filter(lambda x: x, map(islychrel, xrange(10000))))
