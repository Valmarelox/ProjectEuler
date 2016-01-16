
def count_rec(n):
    sum = 0
    if n == 1:
        return 1
    for i in xrange(1, n + 1):
        sum += count_rec(n - i)
    return sum

def s(n):
    if n == 1:
        return 1
    parts = range(2, (n - 2) + 1)
    sum = 2
    for p in parts:
        sum += s(p)
    return sum

print s(100)