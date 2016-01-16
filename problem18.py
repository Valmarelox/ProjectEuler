def load(name):
    f = open(name)
    #lines = f.readlines()
    pyr = []
    for line in f.readlines():
        line = line.replace('\n', '')
        pyr.append([int(x) for x in line.split(' ')])
    f.close()
    return pyr

def rec(pyr, m, n, s):
    if m == len(pyr):
        return 0
    s += pyr[m][n]
    left = rec(pyr, m + 1, n, s)
    right = rec(pyr, m + 1, n + 1, s)
    print left, right, s
    return (s + left if left > right else s + right)


pyr = load('prob18')
print pyr
print rec(pyr,0,0,0)
