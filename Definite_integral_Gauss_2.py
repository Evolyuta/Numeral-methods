import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

plt.rcdefaults()
import numpy as np

x = Symbol('x')

# real answer = 4.46151

n = 2

print('n=', n)

fi = []
fins = []
fijs = []
amatrix = []
point = []

f = lambda t: (4.5 * np.cos(7.0 * (t + 2.1)) * np.exp(-2.0 * (t + 2.1) / 3.0)
               + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3.0) + 3.0)
p = lambda t: (t ** -0.4)

for i in range(2 * n):
    fi.append(1.2 ** (i + 3 / 5) / (i + 3 / 5))

for s in range(0, n):
    fins.append(-fi[n + s])
    dsf = []
    for j in range(0, n):
        dsf.append(fi[j + s])
    fijs.append(dsf)

amatrix.append((fi[0] * fi[3] - fi[2] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))
amatrix.append((fi[2] * fi[2] - fi[3] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))

discr = amatrix[0] * amatrix[0] - 4 * amatrix[1]
point.append((-amatrix[0] - np.sqrt(discr)) / 2)
point.append((-amatrix[0] + np.sqrt(discr)) / 2)

print('points=', point)

pointmatrix = [[1, 1], [point[0], point[1]]]

A2 = (fi[1] - fi[0] * point[0]) / (-point[0] + point[1])
A1 = fi[0] - A2
print('coefs=', A1, A2)

point[0] = float(point[0])
point[1] = float(point[1])

res = A1 * f(point[0]) + A2 * f(point[1])
print('result=', res)
