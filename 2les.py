import numpy as np

import pandas as pd

my_list = [1, 2, 3]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix)

ar2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60], ])
print(ar2d[1][-1])

a = np.array([1, 2, 3, 4])
b = np.array([[5, 6, 7, 8], [9, 10, 11, 12]])
print('==========================')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# print(np.arange(0, 10))
# print()
print('==========================')
# print(np.sqrt(a))
# print(a**b)
# print(np.sin(b))
# print(np.log(b))
zero = np.zeros(10)
print(zero)
ones = np.ones(10)
print(ones)
ones[0:10] = 5
print(ones)
da = np.arange(10, 51, 2)
print(da)
randr = np.arange(9).reshape(3, 3)
print(randr)
ranr2 = np.eye(3, 3)
print(ranr2)
r3 = np.random.rand(1)
print(r3)
r4 = np.random.randn(25)
print(r4)
r5 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(r5)
# print(np.arange(1, 101).reshape(10, 10) / 100)
print(np.linspace(0, 3, 9))
print('==========================')
print(np.linspace(0, 1, 20))
print('==========================')
mat = np.arange(1, 26).reshape(5, 5)

print(mat)
print('==========================')
mat2 = mat[:][2:, 1:]
print(mat2)
print('==========================')
print(mat[3][-1])
print(mat[:3, 1:2])
# print(mat[:3, 1].reshape(3,1))
print(mat[-1])
print('========')
print(mat[4:])
print('======')

chisla = np.random.randint(0, 10, 10)
print(chisla)
ccc = (chisla > 3) & (chisla < 8)
print(ccc)
chisla[ccc] *= -1
print(chisla)

print('=======')
matr = np.arange(1, 26).reshape(5, 5)
print(matr.sum())
print(matr.sum(0))
print(matr.std())
print(matr[::-1])
# bb = [1, 2, 3, 4, 5]
# print(bb[::-1])