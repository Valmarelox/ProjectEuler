
sum_of_fifth_digs = lambda num : sum([int(dig) ** 5 for dig in str(num)])
s = 0
for num in xrange(2, 1000000):
    if num == sum_of_fifth_digs(num):
        s += num
        print s
#print s