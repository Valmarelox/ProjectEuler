#look at this ugly
def pali(a, b):
    aresult = ""
    aresult = str(a * b)
    strlen = len(aresult)
    i = 0
    while i < strlen - i:
        if(aresult[i] != aresult[strlen - i - 1]):
            return 0
        i+=1
    return aresult
a = 100
b = 100
result = 0
highresult = 0

for a in range(100, 999, 1):
    for b in range(100, 999, 1):
        result = int(pali(a, b))
        if(highresult < result):
            highresult = result
print highresult

