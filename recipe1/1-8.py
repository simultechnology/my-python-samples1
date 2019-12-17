import numpy as np

matrix = np.arange(1, 10).reshape((3, 3))
print(matrix)

print(np.mean(matrix))
print(np.var(matrix))
print(np.std(matrix))