
n = 1
fraction = ''
mul = 1
dn = 0
for n in xrange(0, 10 ** 6 + 1):
    fraction += str(n)

for n in xrange(7):
    mul *= (int(fraction[10**n]))
print mul