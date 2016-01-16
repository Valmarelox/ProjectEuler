def digisum(a):
    b = 0
    while a > 1:
        b += a % 10
        a /= 10
    return b

a = 1
b = 1
highdig = 0
currdig = 0
for a in range(1, 100):
    for b in range(1, 100):
        currdig = digisum(a ** b)
        if highdig < currdig:
            highdig = currdig
print highdig
