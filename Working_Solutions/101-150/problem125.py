__author__ = 'efraim'
MAX = 10 ** 8
sqrs = []
x = 1
while x ** 2 <= MAX:
    sqrs.append(x ** 2)
    x+=1

print sqrs
master_sum = 0
count = 0
list_of_already = []
for i,start in enumerate(sqrs):
    s = start
    for to_add in sqrs[i + 1:]:
        s += to_add
        if s>=MAX:
            break
        if str(s) == str(s)[::-1] and s not in list_of_already:
            print s
            master_sum += s
            count += 1
            list_of_already.append(s)

"""for to_add in sqrs[i + 1:]:
        s += to_add
        if s>1000:
            break
        if str(s) == str(s)[::-1]:
            print s
            master_sum += s
            count += 1"""
print "end",master_sum, count