import math
#find line highest base * exp, in a file
def load(name):
    f = open(name, 'r')
    lines = f.readlines()
    f.close()
    pairs = []
    for line in lines:
        pair = line.split(',')
        pair[1] = pair[1][:-1]
        pairs.append((pair))
    return pairs

def getexp(base, exp):
    base10exp = math.log10(float(base))
    print base10exp, exp
    return (base10exp * int(exp))

def find_high(pairs):
    line = 1
    high_line = 0
    high_exp = 0
    for base, exp in pairs:
        exp = getexp(base, exp)
        if exp > high_exp:
            high_exp = exp
            high_line = line
        line += 1
    return high_line

print find_high(load('prob99.txt'))