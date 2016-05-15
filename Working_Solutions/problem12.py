from time import time as t
def factors(n):
    count = 1
    fact = 2
    while n != 1:
        curr_count = 0
        while n % fact == 0:
            n /= fact
            curr_count += 1
        count *= (curr_count + 1 if curr_count != 0 else 1)
        fact += 1
    return count

s = t()
n = 1
i = 2
while 1:
    n += i
    i += 1
    f = factors(n)
    #if f % 20 == 0:
        #print n, f
    if f >= 500:
        print "GOT", n, f, t() - s
        input()
print factors(15802)

