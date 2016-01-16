
def is_bouncy(n):
    dec = True
    inc = True
    j = str(n)[0]
    for i in str(n)[1:]:
        if j > i:
            inc = False
        if j < i:
            dec = False
        j = i
    if dec is False and inc is False:
        return True
    else:
        return False

def prop(a, b):
    return a * 1.00 / b

def count(proportion):
    a = 100
    c = 0
    while 1:
        #print a
        if is_bouncy(a):
            c += 1
            if prop(c, a) == proportion:
                print a, "Very Good"
                input()
        a += 1

#print is_bouncy()
#print prop(1,2) == 0.5
print count(0.99)