#!/usr/bin/python2.7
from tqdm import tqdm
from math import log

def gen_next_fibo():
    k = 1
    a = 1
    b = 1
    while True:
        a, b = b, a + b
        k += 1
        yield a, k

def split_num(a):
    while a > 0:
        yield a % 10
        a /= 10

START = 10 ** 9
def check_pandi_last(a):
    a = a % START 
    return tuple(sorted(split_num(a))) == (1,2,3,4,5,6,7,8,9)

def check_pandi_first(a):
    a = a / (10 ** (int(log(a, 10)) - 8))
    return tuple(sorted(split_num(a))) == (1,2,3,4,5,6,7,8,9)

if __name__ == '__main__':
    res_k = 0
    for (a, k) in tqdm(gen_next_fibo()):
        if check_pandi_last(a) and check_pandi_first(a):
            res_k = k
            break
    print 'Result is ', res_k
