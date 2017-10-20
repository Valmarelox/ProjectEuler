

def load(filename):
    with open(filename, 'r') as f:
        return [map(int, line.split(',')) for line in f.readlines()]


def goRight(matrix, i, j):
    return matrix[i][j] + rec(matrix, i, j + 1)

def goDown(matrix, i, j):
    return matrix[i][j] + rec(matrix, i + 1, j)

def rec(matrix, i, j):
    if i == 79 and j == 79:
        return matrix[i][j]
    if i >= 79:
        return goRight(matrix, i, j)
    if j >= 79:
        return goDown(matrix, i, j)
    first = goRight(matrix, i, j)
    second = goDown(matrix, i, j)
    return first if first < second else second
        
def calc(matrix):
    return rec(matrix, 0, 0)
matrix = load('p081_matrix.txt')

print calc(matrix)
