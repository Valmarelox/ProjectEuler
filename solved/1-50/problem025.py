a, b = 1, 1
c = 0
i = 1
while b < pow(10, 2):
    a, b = a + b, a
    i += 1
    print a, b

print i
