

def tri(n):
    return n * (n + 1) / 2

def pent(n):
    return n * (3 * n - 1) / 2

def hex(n):
    return n * (2 * n - 1)

def check():
    n1 = 1
    n2 = 1
    n3 = 1
    while 1: #tri
        tri_num = tri(n1)
        while 1: #pent
            pent_num = pent(n2)
            if(pent_num > tri_num):
                break
            else:
                n2 += 1
            while 1: #hex
                hex_num = hex(n3)
                print tri_num, pent_num, hex_num
                print n1, n2, n3
                if(pent_num == tri_num == hex_num):
                    print "found:",tri_num
                    n3 += 1
                    input()
                elif(hex_num > pent_num):
                    break
                else:
                    n3 += 1
        n1 += 1

print hex(143)
check()