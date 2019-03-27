import matplotlib.pyplot as plt

plt.rcdefaults()
import numpy as np

# real answer = 4.46151

maxn = 13
ans = []
coefAns = []
maxk = 40
durAns = []  # answer for each section

for n in range(2, maxn):

    print('\n\n\n\nn=', n)

    for currMaxk in range(39, maxk):

        print('k=', currMaxk)
        durAns = []
        h = 1.2 / currMaxk

        for k in range(0, currMaxk):

            firstPoint = k * h
            lastPoint = (k + 1) * h

            fi = []
            point = []
            pointMatrix = []
            strpointMatrix = []
            currAns = 0
            absSumCoef = 0
            duration = lastPoint - firstPoint

            for i in range(n):
                point.append(firstPoint + i * duration / (n - 1))

            # print(point)

            f = lambda t: (4.5 * np.cos(7 * (t + 2.1)) * np.exp(-2 * (t + 2.1) / 3)
                           + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3) + 3)
            p = lambda t: (t ** -0.4)

            for i in range(n):
                fi.append(lastPoint ** (i + 3 / 5) / (i + 3 / 5) - firstPoint ** (i + 3 / 5) / (i + 3 / 5))

            for i in range(n):
                for j in range(n):
                    strpointMatrix.append(point[j] ** i)
                pointMatrix.append(strpointMatrix)
                strpointMatrix = []

            pointMatrix = np.linalg.inv(pointMatrix)

            coefs = np.dot(pointMatrix, fi)

            for i in range(n):
                currAns = currAns + coefs[i] * f(point[i])

            for i in range(n):
                absSumCoef = absSumCoef + abs(coefs[i])

            coefAns.append(absSumCoef)
            # print(' abs coefficient sum=', absSumCoef)
            durAns.append(currAns)

        # print(durAns)
        sumdurAns = 0
        for i in range(len(durAns)):
            sumdurAns = sumdurAns + durAns[i]
        print(' quadrature sum=', sumdurAns)
        ans.append(sumdurAns)

print(len(ans))



args = range(2, maxn)
ords = ans

plt.plot(args, ords, linewidth=2)
plt.ylabel('Quadrature sum')

for i_x, i_y in zip(args, ords):
    if i_x % 1 == 0:
        plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.2f' % i_y))

# args1 = range(2, maxn)
# ords1 = coefAns
#
# plt.plot(args1, ords1, linewidth=2)
# plt.ylabel('blue Quad sum, yellow abs coef sum')
#
# for i_x, i_y in zip(args1, ords1):
#     if i_x % 1 == 0:
#         plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.2f' % i_y))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()

