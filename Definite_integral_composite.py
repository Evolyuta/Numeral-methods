import matplotlib.pyplot as plt

plt.rcdefaults()
import numpy as np

# real answer = 4.46151

maxn = 4
ans = []
coefAns = []
maxk = 51
durAns = []

for n in range(3, maxn):

    print('\n\n\n\nn=', n)

    for currMaxk in range(1, maxk):

        print('k=', currMaxk)
        durAns = []
        h = 1.2 / currMaxk
        print(' h =', h)

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
        print(' Sh1 =', h1Ans)

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
        print(' Sh2 =', h2Ans)
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
        print(' Sh3 =', h3Ans)

        m = -  np.log((h3Ans - h2Ans) / (h2Ans - h1Ans)) / np.log(2)
        eps = 0.000001
        Rh = h1Ans + (h2Ans - h1Ans) / (1 - np.power(2, -m)) - h1Ans
        print(' Rh = ', Rh)
        hopt = h * np.power((eps * (1 - np.power(2, -m)) / abs(h2Ans - h1Ans)), 1 / m)
        print(' hopt = ', hopt)
        print(' m = ', m)

hopt = hopt * 0.95
print("\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\nhopt=",
      hopt)
maxk = int(1.2 / hopt + 0.5)
print('k = ', maxk)
