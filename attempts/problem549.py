#!/usr/bin/env python3
from sympy.ntheory import factorint
from math import factorial, log
from itertools import count
from tqdm import tqdm

MAX = 10 ** 8
def giveall(n):
    return [_get_min(x, n) for x in range(0, int(log(MAX, n)) + 1)]

mem = {

}
def _get_min(n, m):
    if n == 0:
        return 0
    counter = 0
    for x in count(1):
        c = m *x
        while not c % m:
            counter += 1 
            c //= m
            if counter >= n:
                return m * x

def get_min(n, m):
    try:
        return mem[m][n]
    except KeyError:
        mem[m] = giveall(m)
        return mem[m][n]
    

def s(n):
    factors = factorint(n)
    largest_prime = 0
    real = (get_min(count, factor) for factor, count in factors.items())
    return max(real)

def S(n):
    return sum(tqdm(s(i) for i in range(2, n + 1)))

