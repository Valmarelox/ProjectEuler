from scipy.sparse.csgraph import dijkstra,shortest_path
from scipy.sparse import csr_matrix
import numpy as np
mat = []
with open('p081_matrix.txt', 'r') as f:
    for line in f.readlines():
        mat.append(map(int, line.split(',')))

print len(mat), len(mat[0])
m = dijkstra(csr_matrix(mat), indices=0, directed=True)
print m
