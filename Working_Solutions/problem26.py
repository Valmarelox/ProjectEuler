


def countRep(determinant):
    determinant = determinant
    NUMERATOR = 10 ** 2000
    fraction = NUMERATOR / determinant
    fraction = str(fraction)
    #print fraction
    for i, _ in enumerate(fraction):
        if i == 0:
            continue
        rep = fraction[:i]
        repTest = fraction[i : 2 * i]
        if rep == repTest:
            #print i, rep, repTest
            return rep, len(rep)
    #print fraction
    return None, 0
highValue, highRet = 0 ,0

for determinant in xrange(2, 1000):
    _, ret = countRep(determinant)
    if highRet < ret:
        highValue, highRet = determinant,ret

print highValue, highRet
#print countRep(6)