def load(name):
    a = open(name, "rt")
    string = ""
    string = a.readline()
    list = []
    found = 0
    i = 0
    while i < len(string):
        for j in range(i + 1, len(string), 1):
            if(string[j] == ','):
                try:
                    list.append(int(string[i : j]))
                except:
                    break
        i = j
        print i
    return list
a = 10**100000
b = str(a ** 2)
print b
#print load("prob59.txt")
