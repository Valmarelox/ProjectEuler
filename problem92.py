
sqrdig = lambda n: reduce(lambda x, y: x + int(y) ** 2, str(n), 0)

def looper():
    count = 0
    for n in xrange(1, 10000001):
        a = n
        while a != 89 and a != 1:
            a = sqrdig(a)
        if(a == 89):
            count += 1
        print n
    return count

print looper()