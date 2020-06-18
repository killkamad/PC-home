import numpy as np

# Generate a matrix of data
matrix = np.array(
    [[1, 2, 3, 2],
     [3, 2, 1, 6],
     [4, 5, 6, 5]])
print(matrix)
print('==========')
# Find the ordering of the first column (in increasing order)
ind = np.argsort(matrix[:, 0])
print(ind)
print('==========')
# Switch the ordering (so it's decreasing order)
rind = ind[::-1]
print(rind)
print('==========')
# Return the matrix with rows in the specified order
matrix = matrix[rind]
print(matrix)
print('==========')
print(len(matrix[0]))