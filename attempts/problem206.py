from tqdm import tqdm
from math import sqrt
from itertools import permutations, product


target =  '1_2_3_4_5_6_7_8_9_0'
HIGHEST_TARGET = 1929394959697989990
LOWEST_TARGET =  1020304050607080900


RANGE_BOTTOM = int(sqrt(LOWEST_TARGET) - 1)
RANGE_TOP = int(sqrt(HIGHEST_TARGET) - 1)

def gen_numbers():
    #return permutations(range(10), 9)
    return product(*((range(10),) * 9))

def place(x, n):
    return x * (10 ** n)

def gen_num(x):
    assert len(x) == 9
    return 1020304050607080900 + place(x[-1], 1) + place(x[-2], 3) + place(x[-3], 5) + place(x[-4], 7) +  place(x[-5], 9) + \
            place(x[-6], 11) + place(x[-7], 13) +  place(x[-8], 15) + place(x[-9], 17)


for x in tqdm(gen_numbers()):
    n = gen_num(x)
    n_sq = sqrt(n)
    if n_sq.is_integer() and n_sq ** 2 == n:
        print n, sqrt(n)
    

