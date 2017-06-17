from itertools import count

perms = {}
GOAL = 5

def calc(i):
    a = pow(i, 3)
    permutated = ''.join(sorted(str(a)))
    if permutated not in perms:
        perms[permutated] = [i]
    else:
        perms[permutated].append(i)
        if len(perms[permutated]) == GOAL:
            print perms[permutated], map(lambda x: x ** 3, perms[permutated])
            exit(0)


i = 0
try:
    for i in count(1):
        calc(i)
except KeyboardInterrupt:
    print 'reached %d' % i
