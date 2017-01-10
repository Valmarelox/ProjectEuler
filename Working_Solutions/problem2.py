def fibo(max_term):
    a, b = 1, 1
    while a < max_term:
        a, b = b, a + b
        yield a


print sum(x for x in fibo(4 * 10 ** 6) if x % 2 == 0)
