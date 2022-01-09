
def fact(a):
    return reduce(lambda x, y: x * y, xrange(2, a + 1), 1)
def C(n, k):
    return (fact(n)) / (fact(k) * (fact(n - k)))

def find():
    count = 0
    for n in xrange(1, 101):
        for k in xrange(1, n):
            if(C(n, k) > 1000000):
                count+=1
    return count

print find()