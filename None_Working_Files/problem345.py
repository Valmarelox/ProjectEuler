def load():
    f = open('prob345.txt', 'r')
    lines = f.readlines()
    mat = []
    f.close()
    for line in lines:
        mat.append(line.split())
    return mat

def do(mat):
    used_cols = []
    s = 0
    for line in mat:
        currline = [int(x) for x in line]
        while 1:
            high = max(currline)
            if line.index(str(high)) not in used_cols:
                used_cols.append(line.index(str(high)))
                print high
                s += high
                break
            else:
                del currline[currline.index(high)]
    return s

print do(load())