import numpy as np


def problem_e(n):
    b = []
    for i in range(n):
        for j in range(n):
            b.append(j + 1)
    b = np.array(b)
    return b.reshape(n, n)


if __name__ == '__main__':
    print(problem_e(3))
