import numpy as np

matrix = np.arange(1, 10).reshape((3, 3))
print(matrix)

print(np.max(matrix))
print(np.min(matrix))

print(np.max(matrix, axis=0))
print(np.min(matrix, axis=1))
