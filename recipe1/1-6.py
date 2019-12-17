import numpy as np

# 行列を作成
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

add_100 = lambda i: i + 100
print(add_100(1))

vectorized_add_100 = np.vectorize(add_100)
added_100_matrix = vectorized_add_100(matrix)
print(added_100_matrix)

print(matrix + 100)
