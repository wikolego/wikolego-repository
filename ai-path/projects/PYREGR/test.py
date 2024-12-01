# https://pl.spoj.com/problems/PYREGR/

import numpy as np

# tab = np.zeros((3, 3))

# tab[0, 2] = 1
# tab[1, 2] = 2
# tab[2, 2] = 3

# for x in tab:
#     # for y in x:
    # print(x)


# Given 1D array (or flat list)
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr * 10 + np.array([6, 5, 4, 3, 2, 1]))

# Desired dimensions
N = 2  # Number of rows
M = 3  # Number of columns

# Convert the 1D array to a NxM matrix
matrix = np.reshape(arr, (N, M))

print(matrix)