#!/usr/bin/env python3
from math import log, floor
from itertools import count

def get_digit_count(num):
    return int(log(num, 10)) + 1

def get_prefix(num, prefix_len):
    return int(num // (10 ** (get_digit_count(num) - prefix_len)))


def find_lowest(prefix):
    prefix_len = get_digit_count(prefix)
    i = 0
    last = 0
    s = 0
    last_diff = 0
    for k in count(0):
        num = 2 ** k
        p = get_prefix(num, prefix_len)
        if p == prefix:
            i += 1
            print(k, i, k - last)
            if last_diff == k - last == 485:
                print('Hey', k, i)
            last_diff = k - last
            last = k

def get_chain_len(start):
    return 4 * (5 ** start)

def get_generator(start):
    chain_len = get_chain_len(start)
    def generator(index):
        index -= start
    return generator


from tqdm import tqdm

def play(start, hops, prefix):
    curr = start
    nu = 2 ** (curr)
    prefix_len = get_digit_count(prefix)
    l = []
    for i in count(1):
        for hop in hops:
            nu1 = nu * (hops[hop])
            p = get_prefix(nu1, prefix_len)
            if p == prefix:
                print(i, curr)
                curr += hop
                nu = nu1
                l.append(hop)
                break
        else:
            print('FUCK', i)
            return
        if i == 2000:
            return l



def do():
    return play(90, {hop:2**hop for hop in (485, 289, 196)}, 123)
