
def do():
    a = 2
    b = 1
    count = 1
    while a < 10:
        b = 1
        while b < 10:
            print a, b ,a ** b,len(str(a**b))
            if b == len(str(a**b)):
                count += 1
            b += 1
        a+= 1
    return count

print do()