import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def reg1dim1(x, y):
    a = np.dot(x, y) / (x**2).sum()
    return a

def reg1dim2(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum() / n) / ((x**2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum()) / n
    return a, b


x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5 ,4])
a = reg1dim1(x, y)
print(a)

plt.scatter(x=x, y=y)
xmax = x.max()
plt.plot([0, xmax], [0, a*xmax])
plt.show()


# A = np.array([[1,1], [2,2]])
# B = np.array([[1, 2], [3, 4]])
# print(np.dot(A, B))
#
# print(A * B)

def least_square(x, y):
    xmean = x.mean()
    ymean = y.mean()

    numerator_arr = np.array([xelem - xmean for xelem in x]) * np.array([yelem - ymean for yelem in y])
    denominator_arr = np.array([(xelem - xmean) ** 2 for xelem in x])

    numerator = numerator_arr.sum()
    denominator = denominator_arr.sum()

    b1 = numerator / denominator
    b0 = ymean - b1 * xmean
    return b1, b0

# b = least_square(x, y)
# print(b)

def get_coefficients(X, Y):
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    m = len(X)
    numer = 0
    denom = 0
    for i in range(m):
        numer += (X[i] - mean_x) * (Y[i] - mean_y)
        denom += (X[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
    return b1, b0

# b1 = get_coefficients(x, y)
# print(b)

print('-------data from csv-------')

df = pd.read_csv('headbrain.csv')
X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values

b1, b0 = get_coefficients(X, Y)
print(b1, b0)

my_coeff = least_square(X, Y)
print(my_coeff)

my_coeff2 = reg1dim2(X, Y)
print(my_coeff2)

#plotting values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

#Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1*x

#Plot Scatter points
plt.scatter(X, Y, c ='#ef5423', label = 'Scatter Plot')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')

plt.plot(x, y, color='b', label='Regression Line')
plt.legend()
plt.show()
