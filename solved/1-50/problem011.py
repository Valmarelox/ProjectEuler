def getmat(name):
    grid = open(name, "rt")
    matgrid = [[]]
    i = 0
    c = 0
    for a in grid.readlines():
        for b in a:
            if b == '\n':
                matgrid.append([])
                i+=1
            elif b == ' ':
                continue
            elif c != 0:
                matgrid[i].append(int(c + b))
                c = 0
            else:
                c = b
    return matgrid

def horizontaly(grid):
    highmul = 0
    for i in range(20):
        for j in range(20):
            if 20 > j + 4:
                mul = grid[i][j] * grid[i][j +1] * grid[i][j + 2] * grid[i][j + 3]
                if mul > highmul:
                    highmul = mul
                    #print i, j, grid[i][j]
    return highmul
def verticaly(grid):
    highmul = 0
    placei, placej, number = 0, 0, 0
    for i in range(20):
        for j in range(20):
            if len(grid) > j + 4:
                mul = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
                if mul > highmul:
                    highmul = mul
    return highmul
def diagonal(grid):
    highmul = 0
    for i in range(0, 20, 1):
        for j in range(0, 20, 1):
            if len(grid) > j + 4 and len(grid) > i + 4:
                mul = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
                if mul > highmul:
                    highmul = mul
            if i - 4 > 0 and len(grid) > j + 4:
                mul = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
                if mul > highmul: highmul = mul
    return highmul

grid = getmat("prob11.txt")
highhor =  horizontaly(grid)
highver = verticaly(grid)
highdia = diagonal(grid)
print "highhor:", highhor, "highver:", highver, "highdia:", highdia