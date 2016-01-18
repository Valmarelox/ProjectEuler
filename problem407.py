
def M(mod):
    high = 0
    for a in xrange(0, mod):
        if( (a ** 2) % mod == a % mod and a % mod > high):
            high = a % mod
        elif mod < high:
            break
    return high

sigma = 0
for n in xrange(10**7):
    if(n % 100000 == 0):
        print n
    sigma += M(n)
print sigma