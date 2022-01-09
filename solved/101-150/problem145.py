

def reverse(n):
	return int(str(n)[::-1]) 

def isOnlyOdd(n):
	return reduce(lambda x, y: x and int(y) % 2 != 0, str(n), True)

def canReverse(n):
	return n % 10 != 0

def isGood(n):
	return canReverse(n) and isOnlyOdd(n + reverse(n))

print isGood(36)

l = xrange(1, 10 ** 9)
li = []
for x in l:
	if isGood(x):
		li.append(x)
	
s = li
#s = filter(lambda x: isGood(x), l)
print s
print len(s)
