import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

plt.rcdefaults()
import numpy as np
x = Symbol('x')

# real answer = 4.46151

maxn = 3
ans = []
coefAns = []

for n in range(2, maxn):

    print('n=', n)

    fi = []
    point = []
    pointmatrix = []
    strpointmatrix = []
    currAns = 0
    absSumCoef = 0
    fins=[]
    fijs=[]
    amatrix=[]

    # for i in range(n):
    #     point.append(i * 1.2 / (n - 1))

    f = lambda t: (4.5 * np.cos(7.0* (t + 2.1)) * np.exp(-2.0 * (t + 2.1) / 3.0)
                   + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3.0) + 3.0)
    p = lambda t: (t ** -0.4)

    for i in range(2*n):
        fi.append(1.2 ** (i + 3 / 5) / (i + 3 / 5))

    print(fi)

    for s in range (0,n):
        fins.append(-fi[s])
        dsf=[]
        for j in range (0,n):
            dsf.append(fi[j+s])
        fijs.append(dsf)

    print('fijs=',fijs)

    amatrix=(np.dot(fins,np.linalg.inv(fijs)))
    print('amtr=',amatrix)
    print('dot=',np.dot(amatrix,fijs))
    eq = amatrix[0]
    for i in range(1, maxn - 1):
        eq = x ** i * amatrix[i] + eq
    eq = x ** n + eq
    # print(eq)

    point = solve(eq)

    print('x=',point)
    #
    for i in range(n):
        for j in range(n):
            point[j]=float(point[j])
            strpointmatrix.append(point[j] ** i)
        pointmatrix.append(strpointmatrix)
        strpointmatrix = []

    print(pointmatrix)

    for i in range(n):
        for j in range(n):
            pointmatrix[i][j]=float(pointmatrix[i][j])

    pointmatrix = np.linalg.inv(pointmatrix)

    coefs = np.dot(pointmatrix, fijs)

    print(coefs)


    for i in range(n):
        currAns = currAns + coefs[i] * f(point[i])

    print(currAns)

    """

    for i in range(n):
        for j in range(n):
            strpointmatrix.append(point[j] ** i)
        pointmatrix.append(strpointmatrix)
        strpointmatrix = []

    pointmatrix = np.linalg.inv(pointmatrix)

    coefs = np.dot(pointmatrix, fi)

    for i in range(n):
        currAns = currAns + coefs[i] * f(point[i])

    for i in range(n):
        absSumCoef = absSumCoef + abs(coefs[i])

    ans.append(currAns)
    coefAns.append(absSumCoef)
    print(' quadrature sum=', currAns)
    print(' abs coefficient sum=', absSumCoef)

args = range(2, maxn)
ords = ans

plt.plot(args, ords, linewidth=2)
plt.ylabel('Quadrature sum')

for i_x, i_y in zip(args, ords):
    if i_x % 1 == 0:
        plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.2f' % i_y))

args1 = range(2, maxn)
ords1 = coefAns

plt.plot(args1, ords1, linewidth=2)
plt.ylabel('blue Quad sum, yellow abs coef sum')

for i_x, i_y in zip(args1, ords1):
    if i_x % 1 == 0:
        plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.2f' % i_y))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
"""