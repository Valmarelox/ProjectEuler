from tqdm import tqdm
from sympy import sieve

MAX = 10000


for x in tqdm(sieve.primerange(1000, MAX)):
    for y in sieve.primerange(x + 1, MAX):
        z = y + y - x

        if z in sieve:
            if sorted(str(x)) == sorted(str(y)) == sorted(str(z)):
                print 'GOT ', x, y, z
                print 'FIND', str(x) + str(y) + str(z)


