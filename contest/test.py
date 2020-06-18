# import numpy as np
#
# # Generate a matrix of data
# matrix = np.random.rand(5,4)
# print(matrix)
# # Find the ordering of the first column (in increasing order)
# ind = np.argsort(matrix[:,0])
# print(ind)
# # Switch the ordering (so it's decreasing order)
# rind = ind[::-1]
# print(rind)
# # Return the matrix with rows in the specified order
# matrix = matrix[rind]
# print(matrix)


# MAX = 100
# mat = [[0 for x in range(MAX)] for y in range(MAX)]
#
#
# def fillRemaining(i, j, n):
#     x = 2
#
#     for k in range(i + 1, n):
#         mat[k][j] = x
#         x += 1
#     for k in range(i):
#         mat[k][j] = x
#         x += 1
#
#
# def constructMatrix(n):
#     right = n - 1
#     left = 0
#     for i in range(n):
#         if (i % 2 == 0):
#             mat[i][right] = 1
#             fillRemaining(i, right, n)
#             right -= 1
#         else:
#             mat[i][left] = 1
#             fillRemaining(i, left, n)
#             left += 1
#
#
# n = 3
#
# constructMatrix(n)
#
# for i in range(n):
#     for j in range(n):
#         print(mat[i][j], end=" ")
#     print("")


def lower_upper(s):
    change = []

    for char in s:
        if char.islower():
            change.append(char.upper())
        elif char.isupper():
            change.append(char.lower())
        else:
            change.append(char)

    return ''.join(change)


if __name__ == '__main__':
    print(lower_upper("AliK"))
