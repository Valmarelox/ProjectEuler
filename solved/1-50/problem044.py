from math import sqrt
pentagon = lambda n: n * (3 * n - 1) / 2
pentagons = set()

def generatePentagons():
    n = 1
    while 1:
        p = pentagon(n)
        pentagons.add(p)
        yield p
        n += 1

def isPentagon(p):
    if p in pentagons:
        return True
    sqr = sqrt(1 + 24 * p)
    if not sqr.is_integer():
        return False
    n = ((1 + sqr) / 6)
    if n.is_integer():
        pentagons.add(p)
        return True
    else:
        return False

def iterateOnSet(p1):
    try: 
        for p2 in pentagons:
            if p1 != p2 and isPentagon(abs(p1 - p2)) and isPentagon(p1 + p2):
                print 'nums:', p1, p2
                print 'sum', p1 + p2
                print 'diff', abs(p1 - p2)
                raw_input()
    except RuntimeError:
        iterateOnSet(p1)

for p1 in generatePentagons():
    iterateOnSet(p1)
