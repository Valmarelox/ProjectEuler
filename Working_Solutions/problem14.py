import time
def collatz(n):
    chain = 1
    while n != 1:
        #print n, ", ",
        if n % 2:
            n = 3*n + 1
        else:
            n /= 2
        chain += 1

    return chain

def check():
    highchain = 0
    highnum = 0
    for n in range(3, 1000001, 1):
        currchain =collatz(n)
        if currchain > highchain:
            highchain = currchain
            highnum = n
    return highnum

start = time.time()
#print collatz(13)
print check(), time.time() - start
