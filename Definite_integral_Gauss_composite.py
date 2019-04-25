import matplotlib.pyplot as plt
import numpy as np

# real answer = 4.46151

maxn = 3
ans = []
coefAns = []
maxk = 20
durAns = []
currMaxk=2
Rh=1


epsArray = []
hoptArray = []

eps = 1.0e-5

while (eps>1.0e-8):

    print(eps)

    for n in range(2, maxn):

        # print('\n\n\n\nn=', n)

        while (abs(Rh)>eps):

        # for currMaxk in range(1, maxk):

            maxk=currMaxk

            # print('k=', currMaxk)
            durAns = []
            h = 1.2 / currMaxk
            # print(' h =', h)

            h1 = h

            for k in range(0, currMaxk):

                firstPoint = k * h1
                lastPoint = (k + 1) * h1

                fi = []
                amatrix = []
                point = []

                f = lambda t: (4.5 * np.cos(7.0 * (t + 2.1)) * np.exp(-2.0 * (t + 2.1) / 3.0)
                               + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3.0) + 3.0)
                p = lambda t: (t ** -0.4)

                for i in range(2 * n):
                    fi.append(lastPoint ** (i + 3 / 5) / (i + 3 / 5) - firstPoint ** (i + 3 / 5) / (i + 3 / 5))

                amatrix.append((fi[0] * fi[3] - fi[2] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))
                amatrix.append((fi[2] * fi[2] - fi[3] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))

                discr = amatrix[0] * amatrix[0] - 4 * amatrix[1]
                point.append((-amatrix[0] - np.sqrt(discr)) / 2)
                point.append((-amatrix[0] + np.sqrt(discr)) / 2)

                A2 = (fi[1] - fi[0] * point[0]) / (-point[0] + point[1])
                A1 = fi[0] - A2

                point[0] = float(point[0])
                point[1] = float(point[1])

                res = A1 * f(point[0]) + A2 * f(point[1])
                durAns.append(res)

            h1Ans = 0
            for i in range(len(durAns)):
                h1Ans = h1Ans + durAns[i]
            # print(' Sh1 =', h1Ans)
            h1Ans = float(h1Ans)

            h2 = h / 2
            currMaxk = currMaxk * 2
            durAns = []

            for k in range(0, currMaxk):

                firstPoint = k * h2
                lastPoint = (k + 1) * h2

                fi = []
                amatrix = []

                f = lambda t: (4.5 * np.cos(7.0 * (t + 2.1)) * np.exp(-2.0 * (t + 2.1) / 3.0)
                               + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3.0) + 3.0)
                p = lambda t: (t ** -0.4)

                for i in range(2 * n):
                    fi.append(lastPoint ** (i + 3 / 5) / (i + 3 / 5) - firstPoint ** (i + 3 / 5) / (i + 3 / 5))

                amatrix.append((fi[0] * fi[3] - fi[2] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))
                amatrix.append((fi[2] * fi[2] - fi[3] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))

                point = []
                discr = amatrix[0] * amatrix[0] - 4 * amatrix[1]
                point.append((-amatrix[0] - np.sqrt(discr)) / 2)
                point.append((-amatrix[0] + np.sqrt(discr)) / 2)

                A2 = (fi[1] - fi[0] * point[0]) / (-point[0] + point[1])
                A1 = fi[0] - A2

                point[0] = float(point[0])
                point[1] = float(point[1])

                res = A1 * f(point[0]) + A2 * f(point[1])
                durAns.append(res)

            h2Ans = 0
            for i in range(len(durAns)):
                h2Ans = h2Ans + durAns[i]
            # print(' Sh2 =', h2Ans)
            h2Ans = float(h2Ans)
            h3 = h / 4
            currMaxk = currMaxk * 2
            durAns = []

            for k in range(0, currMaxk):

                firstPoint = k * h3
                lastPoint = (k + 1) * h3

                fi = []
                amatrix = []

                f = lambda t: (4.5 * np.cos(7.0 * (t + 2.1)) * np.exp(-2.0 * (t + 2.1) / 3.0)
                               + 1.4 * np.sin(1.5 * (t + 2.1)) * np.exp(-(t + 2.1) / 3.0) + 3.0)
                p = lambda t: (t ** -0.4)

                for i in range(2 * n):
                    fi.append(lastPoint ** (i + 3 / 5) / (i + 3 / 5) - firstPoint ** (i + 3 / 5) / (i + 3 / 5))

                amatrix.append((fi[0] * fi[3] - fi[2] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))
                amatrix.append((fi[2] * fi[2] - fi[3] * fi[1]) / (fi[1] ** 2 - fi[0] * fi[2]))

                point = []
                discr = amatrix[0] * amatrix[0] - 4 * amatrix[1]
                point.append((-amatrix[0] - np.sqrt(discr)) / 2)
                point.append((-amatrix[0] + np.sqrt(discr)) / 2)

                A2 = (fi[1] - fi[0] * point[0]) / (-point[0] + point[1])
                A1 = fi[0] - A2

                point[0] = float(point[0])
                point[1] = float(point[1])

                res = A1 * f(point[0]) + A2 * f(point[1])
                durAns.append(res)

            h3Ans = 0
            for i in range(len(durAns)):
                h3Ans = h3Ans + durAns[i]
            h3Ans = float(h3Ans)
            # print(' Sh3 =', h3Ans)

            m = - np.log((h3Ans - h2Ans) / (h2Ans - h1Ans)) / np.log(2)
            # eps = 0.000001
            Rh = h1Ans + (h2Ans - h1Ans) / (1 - np.power(2, -m)) - h1Ans
            # print(' Rh = ', Rh)
            hopt = h * np.power((eps * (1 - np.power(2, -m)) / abs(h2Ans - h1Ans)), 1 / m)
            # print(' hopt = ', hopt)
            # print(' m = ', m)
            currMaxk = maxk+1

    hopt = hopt * 0.95
    print("\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\nhopt=",
          hopt)
    # maxk = int(1.2 / hopt + 0.5)
    # print('k = ', maxk)
    epsArray.append(eps)
    hoptArray.append(hopt)
    eps = eps / 1.5

print(hoptArray)

args = range(6,17)
ords = hoptArray[6:17]


plt.plot(args, ords, linewidth=2)
plt.ylabel('Quadrature sum')

for i_x, i_y in zip(args, ords):
    if i_x % 1 == 0:
        plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.5f' % i_y))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()