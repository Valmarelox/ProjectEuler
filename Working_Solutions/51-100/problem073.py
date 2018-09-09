#!/usr/bin/python3.6
from tqdm import tqdm
from math import gcd

'''
Optimizations:
    1. don't use fraction
    2. do range in loop, check gcd with python3.5
'''
MAX_D = 12000

c = 0
for d in tqdm(range(3, MAX_D + 1)):
    for n in range(int((d / 3) + 1), int((d / 2) + 1)):
        if gcd(n, d) != 1:
            continue
        c+=1 

print(c)
