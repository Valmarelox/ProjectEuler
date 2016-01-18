from itertools import permutations

pergen = permutations("0123456789")
i = 0
while(i < 10 ** 6 - 1):
    pergen.next()
    i+=1
print pergen.next()