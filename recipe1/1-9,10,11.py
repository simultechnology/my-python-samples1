import numpy as np

Matrix = np.arange(1, 13).reshape(4, 3)
print(Matrix)
print(Matrix.reshape(2, -1))

print(Matrix.T)

a = np.array([np.arange(1,7)])

print(a)
print(a.T)

print(Matrix)
print(Matrix.flatten())