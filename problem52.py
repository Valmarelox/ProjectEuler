
sort = lambda x: sorted(str(x))
def do():
    x = 1
    while 1:
        print x
        if(sort(x) == sort(2 * x) == sort(3 * x) == sort(4 * x) == sort(5 * x) == sort(6 * x)):
            print "found",x
            break
        x += 1

do()