prob8 = open("prob8.txt", "r")
a = "a"
b = 'b'
mul = 1
maxmul = 1
offset = 0
while a != "":
    a = prob8.read(13)
    for b in a:
        print b
        if b != "":
            #print b
            mul *= int(b)
    if mul > maxmul:
        maxmul = mul
    offset += 1
    mul = 1
    prob8.seek(offset, 0)
print maxmul
