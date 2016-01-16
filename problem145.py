def check(n):
    if str(n)[-1] == '0':
        return False
    s = (n + int(str(n)[::-1]))
    for i in str(s):
        if int(i) % 2 == 0:
            return False
    return True

s = 0
for i in xrange(10 ** 9):
    if check(i):
        s += 1

print s