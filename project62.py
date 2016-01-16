from itertools import permutations

a = 345
while 1:
    count = 0
    for perm in permutations(str(a ** 3)):
        perm = ''.join(perm)
        base = float(int(perm) ** (1 / 3.0))
        print base
        if base == int(base):
            count += 1
    if count == 3 or count == 5:
        print a ** 3, count
    print a, count
    exit()