import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

A = 3
B = 1
C = 3

tol = 1e-5
rtol = 1e-6
atol = 1e-12
p = 2

c2 = 0.35
b2 = 1 / (2 * c2)
b1 = 1 - b2

x0 = 0
xn = 5

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

f1 = lambda x, y1, y2, y3, y4: 2 * x * y4 * y2 ** (1 / B)
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B * (y3 - A) / C) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)


def step(x0, y10, y20, y30, y40, h):
    y11 = y10 + h * (b1 * f1(x0, y10, y20, y30, y40) +
                     b2 * f1(x0 + h * c2,
                             y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                             y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                             y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                             y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    y21 = y20 + h * (b1 * f2(x0, y10, y20, y30, y40) +
                     b2 * f2(x0 + h * c2,
                             y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                             y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                             y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                             y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    y31 = y30 + h * (b1 * f3(x0, y10, y20, y30, y40) +
                     b2 * f3(x0 + h * c2,
                             y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                             y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                             y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                             y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    y41 = y40 + h * (b1 * f4(x0, y10, y20, y30, y40) +
                     b2 * f4(x0 + h * c2,
                             y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                             y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                             y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                             y40 + h * c2 * f4(x0, y10, y20, y30, y40)))

    return (y11, y21, y31, y41)


def firstStep(x0, xk, y10, y20, y30, y40):
    f10 = f1(x0, y10, y20, y30, y40)
    f20 = f2(x0, y10, y20, y30, y40)
    f30 = f3(x0, y10, y20, y30, y40)
    f40 = f4(x0, y10, y20, y30, y40)

    delta = np.power(max(abs(x0), abs(xk)), -(p + 1)) + np.power(np.sqrt(f10 * f10 + f20 * f20 + f30 * f30 + f40 * f40),
                                                                 (p + 1))

    h1 = np.power((tol / delta), 1 / (p + 1))

    return h1


globalNormArray = []
acceptArray = []
hArray = []
xArray = []
k = 0

"""Находим первый шаг"""
xk = 1e-3

y10 = y1(x0)
y20 = y2(x0)
y30 = y3(x0)
y40 = y4(x0)

h = firstStep(x0, xk, y10, y10, y30, y40)

xk = x0 + h

(y10, y20, y30, y40) = step(x0, y10, y20, y30, y40, h)
h1stroke = firstStep(x0, xk, y10, y10, y30, y40)

h = min(h, h1stroke)
""""--"""

y10 = y1(x0)
y20 = y2(x0)
y30 = y3(x0)
y40 = y4(x0)

while (x0 < xn):

    print(k)
    k = k + 1
    print('x0, h', x0, h)
    xArray.append(x0)
    hArray.append(h)

    hhalf = h / 2

    (y1halfstep, y2halfstep, y3halfstep, y4halfstep) = step(x0, y10, y20, y30, y40, hhalf)

    x1half = x0 + hhalf

    (y1doublestep, y2doublestep, y3doublestep, y4doublestep) = step(x1half, y1halfstep, y2halfstep, y3halfstep,
                                                                    y4halfstep, hhalf)

    (y1singlestep, y2singlestep, y3singlestep, y4singlestep) = step(x0, y10, y20, y30, y40, h)

    rn1 = (y1singlestep - y1doublestep) ** 2 / (1 + 2 ** (-p))
    rn2 = (y2singlestep - y2doublestep) ** 2 / (1 + 2 ** (-p))
    rn3 = (y3singlestep - y3doublestep) ** 2 / (1 + 2 ** (-p))
    rn4 = (y4singlestep - y4doublestep) ** 2 / (1 + 2 ** (-p))

    x0 = x0 + h

    rnNorm = np.sqrt(rn1 ** 2 + rn2 ** 2 + rn3 ** 2 + rn4 ** 2)

    if (rnNorm > tol * 2 ** p):
        acceptArray.append(0)
        h = hhalf
        x0 = x0 - h
    elif (rnNorm > tol):
        acceptArray.append(0)
        h = hhalf
        (y10, y20, y30, y40) = (y1doublestep, y2doublestep, y3doublestep, y4doublestep)
    elif (rnNorm > tol * 2 ** (p + 1)):
        acceptArray.append(0)
        (y10, y20, y30, y40) = (y1singlestep, y2singlestep, y3singlestep, y4singlestep)
    else:
        acceptArray.append(1)
        h = 2 * h
        (y10, y20, y30, y40) = (y1singlestep, y2singlestep, y3singlestep, y4singlestep)

    rglobal1 = (y10 - y1(x0)) ** 2
    rglobal2 = (y20 - y2(x0)) ** 2
    rglobal3 = (y30 - y3(x0)) ** 2
    rglobal4 = (y40 - y4(x0)) ** 2

    globalNorm = np.sqrt(rglobal1 ** 2 + rglobal2 ** 2 + rglobal3 ** 2 + rglobal4 ** 2)
    print(globalNorm)

    globalNormArray.append(globalNorm)

args = xArray
ords = hArray

plt.plot(args, ords, linewidth=2)

for i_x, i_y, accept in zip(args, ords, acceptArray):
    if accept == 1:
        plt.text(i_x, i_y, '*')
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
