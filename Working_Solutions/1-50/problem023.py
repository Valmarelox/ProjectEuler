from time import time
UPPER_LIMIT = 28123

def get_proper_divisors(n):
    for num in xrange(1, n / 2 + 1):
        if n % num == 0:
            yield num


def get_abundant_num():
    start = time()
    for n in xrange(2, UPPER_LIMIT):
        if sum(get_proper_divisors(n)) > n:
            yield n
    print "generator finished in ", time() - start


abundants = list(get_abundant_num())
start = time()
print abundants
nums = [False] * UPPER_LIMIT
for i, a in enumerate(abundants):
    for b in abundants[i:]:
        try:
            nums[a + b] = True
        except:
            pass
print 'finished loop in', time() - start
#print nums
print sum(map(lambda x : x[0] if not x[1] else 0, enumerate(nums)))
