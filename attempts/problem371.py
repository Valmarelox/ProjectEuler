from fractions import Fraction
from itertools import product

PRECISION=10

p = Fraction(1, 1000)
n_p = 1 - p
t_chance = 0
for op in product((p, n_p), repeat=10):
    chance = 1
    first = False
    for c in op:
        chance *= c
        if c == p:
            if first:
                break
            else:
                first = True
    t_chance += chance

print chance, float(chance)
