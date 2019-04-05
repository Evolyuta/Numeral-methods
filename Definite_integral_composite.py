import matplotlib.pyplot as plt
import numpy as np

# real answer = 4.46151

maxn = 3
ans = []
coefAns = []
maxk = 51
durAns = []
currMaxk = 5
Rh = 1

epsArray = []
hoptArray = []

eps = 1.0e-5

while (eps>1.0e-8):

    print('eps=',eps)

    for n in range(maxn, maxn+1):

        # print('\n\n\n\nn=', n)

        while (abs(Rh) > eps):

            # for currMaxk in range(1, maxk):

            maxk = currMaxk

            print('k=', currMaxk)
            durAns = []
            h = 1.2 / currMaxk
            # print(' h =', h)

            for k in range(0, currMaxk):

                firstPoint = k * h
                lastPoint = (k + 1) * h

                fi = []
                point = []
                pointMatrix = []
                strpointMatrix = []
                currAns = 0
                duration = lastPoint - firstPoint

                for i in range(n):
                    point.append(firstPoint + i * duration / (n - 1))

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

                durAns.append(currAns)

            h1Ans = 0
            for i in range(len(durAns)):
                h1Ans = h1Ans + durAns[i]
            # print(' Sh1 =', h1Ans)

            h2 = h / 2
            currMaxk = currMaxk * 2
            durAns = []

            for k in range(0, currMaxk):

                firstPoint = k * h2
                lastPoint = (k + 1) * h2

                fi = []
                point = []
                pointMatrix = []
                strpointMatrix = []
                currAns = 0
                duration = lastPoint - firstPoint

                for i in range(n):
                    point.append(firstPoint + i * duration / (n - 1))

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

                durAns.append(currAns)

            h2Ans = 0
            for i in range(len(durAns)):
                h2Ans = h2Ans + durAns[i]
            # print(' Sh2 =', h2Ans)
            h3 = h / 4
            currMaxk = currMaxk * 2
            durAns = []

            for k in range(0, currMaxk):

                firstPoint = k * h3
                lastPoint = (k + 1) * h3

                fi = []
                point = []
                pointMatrix = []
                strpointMatrix = []
                currAns = 0
                duration = lastPoint - firstPoint

                for i in range(n):
                    point.append(firstPoint + i * duration / (n - 1))

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

                durAns.append(currAns)

            h3Ans = 0
            for i in range(len(durAns)):
                h3Ans = h3Ans + durAns[i]
            # print(' Sh3 =', h3Ans)

            m = -  np.log((h3Ans - h2Ans) / (h2Ans - h1Ans)) / np.log(2)
            Rh = h1Ans + (h2Ans - h1Ans) / (1 - np.power(2, -m)) - h1Ans
            # print(' Rh = ', Rh)
            hopt = h * np.power((eps * (1 - np.power(2, -m)) / abs(h2Ans - h1Ans)), 1 / m)
            # print(' hopt = ', hopt)
            # print(' m = ', m)
            currMaxk = int(1.2 / hopt + 1.5)#maxk + 1

    # hopt = hopt * 0.95
    print("\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\nhopt=",
          hopt)
    maxk = int(1.2 / hopt + 0.5)
    epsArray.append(eps)
    hoptArray.append(hopt)
    eps=eps/1.5


# print(epsArray,hopt)

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