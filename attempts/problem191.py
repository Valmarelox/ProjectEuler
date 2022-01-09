import itertools
import re
found = []
count = 0
for L in xrange(0, 2):
    for A in xrange(0, 4 - L):
        print
        O = 4 - L - A
        string = 'L' * L + 'O' * O + 'A' * A
        perms = itertools.permutations(list(string))
        if len(string) != 4:
            print 'LOL', L, A, O
            continue
        for option in perms:
            print option
           # print string, option
            if option in found:
                break
            toMuchAbs = option.count('A')
            if toMuchAbs < 3:
                found.append(option)
                count += 1

print count