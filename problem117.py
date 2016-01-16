#Project Euler Problem 117

n = 50
ways = [1] + [0] * n
#print ways
for j in range(1, n+1):
    for k in range(1, min(5, j+1)):
        ways[j] += ways[j - k]

print "Space size =", n, "units"
print "Number of ways to fill:",  ways[-1]