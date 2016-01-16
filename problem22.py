def mat2():
    name = open("name", "rt")
    namestr = ""
    names = [""]
    for a in name.readline():
        if(a == ','):
            namestr += "\n"
        elif(a != '\"'):
            namestr += a
    i = 0
    for a in namestr:
        if(a != "\n"):
            names[i] += a
        else:
            i += 1
            names.append("")
    return names

def ordersum(names):
    totalsum = 0
    names.sort()
    for i, name in enumerate(names):
        lettersum = 0
        for letter in name:
            lettersum += (ord(letter) - 64)
        totalsum += (lettersum) * (i + 1)
    return totalsum
#names =mat2()
#names.sort()
#print names
print ordersum(mat2())

