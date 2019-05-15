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

xn = 5

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

f1 = lambda x, y1, y2, y3, y4: 2 * x * y4 * y2 ** (1 / B)
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B * (y3 - A) / C) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)

xArray = []
hArray = []
acceptArray = []

xk = 0

while xk < xn:
    xk = xk + 0.009
    yNorma = np.sqrt(
        y1(xk) ** 2 + y2(xk) ** 2 + y3(xk) ** 2 +
        y4(xk) ** 2)
    print(xk)
    x0 = 0
    y10 = y1(0)
    y20 = y2(0)
    y30 = y3(0)
    y40 = y4(0)

    f10 = f1(x0, y10, y20, y30, y40)
    f20 = f2(x0, y10, y20, y30, y40)
    f30 = f3(x0, y10, y20, y30, y40)
    f40 = f4(x0, y10, y20, y30, y40)

    normaf0 = np.sqrt(f10 ** 2 + f20 ** 2 + f30 ** 2 + f40 ** 2)

    delta = np.power(1 / max(abs(x0), abs(xk)), p + 1) + np.power(normaf0, p + 1)

    h = np.power((tol / delta), 1 / (p + 1))

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

    y10 = y11
    y20 = y21
    y30 = y31
    y40 = y41

    x0 = x0 + h

    f10 = f1(x0, y10, y20, y30, y40)
    f20 = f2(x0, y10, y20, y30, y40)
    f30 = f3(x0, y10, y20, y30, y40)
    f40 = f4(x0, y10, y20, y30, y40)

    normaf0 = np.sqrt(f10 ** 2 + f20 ** 2 + f30 ** 2 + f40 ** 2)

    delta = np.power(1 / max(abs(x0), abs(xk)), p + 1) + np.power(normaf0, p + 1)

    h1stroke = np.power((tol / delta), 1 / (p + 1))

    h1 = min(h, h1stroke)

    h = h1
    x0 = 0
    y10 = y1(0)
    y20 = y2(0)
    y30 = y3(0)
    y40 = y4(0)

    while x0 < xn - h:
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

        # print(x0)

        y10 = y11
        y20 = y21
        y30 = y31
        y40 = y41

        x0 = x0 + h

    xn1 = x0
    yn11 = y10
    yn12 = y20
    yn13 = y30
    yn14 = y40
    hn = h

    # norma = tol * 2 ** p + 1

    # while (norma > tol * 2 ** p):
    h = hn
    x0 = xn1
    y10 = yn11
    y20 = yn12
    y30 = yn13
    y40 = yn14

    ydouble1 = y10 + h * (b1 * f1(x0, y10, y20, y30, y40) +
                          b2 * f1(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ydouble2 = y20 + h * (b1 * f2(x0, y10, y20, y30, y40) +
                          b2 * f2(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ydouble3 = y30 + h * (b1 * f3(x0, y10, y20, y30, y40) +
                          b2 * f3(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ydouble4 = y40 + h * (b1 * f4(x0, y10, y20, y30, y40) +
                          b2 * f4(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))

    h = h / 2

    ysingle1 = y10 + h * (b1 * f1(x0, y10, y20, y30, y40) +
                          b2 * f1(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle2 = y20 + h * (b1 * f2(x0, y10, y20, y30, y40) +
                          b2 * f2(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle3 = y30 + h * (b1 * f3(x0, y10, y20, y30, y40) +
                          b2 * f3(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle4 = y40 + h * (b1 * f4(x0, y10, y20, y30, y40) +
                          b2 * f4(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))

    y10 = ysingle1
    y20 = ysingle2
    y30 = ysingle3
    y40 = ysingle4

    x0 = x0 + h

    ysingle1 = y10 + h * (b1 * f1(x0, y10, y20, y30, y40) +
                          b2 * f1(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle2 = y20 + h * (b1 * f2(x0, y10, y20, y30, y40) +
                          b2 * f2(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle3 = y30 + h * (b1 * f3(x0, y10, y20, y30, y40) +
                          b2 * f3(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))
    ysingle4 = y40 + h * (b1 * f4(x0, y10, y20, y30, y40) +
                          b2 * f4(x0 + h * c2,
                                  y10 + h * c2 * f1(x0, y10, y20, y30, y40),
                                  y20 + h * c2 * f2(x0, y10, y20, y30, y40),
                                  y30 + h * c2 * f3(x0, y10, y20, y30, y40),
                                  y40 + h * c2 * f4(x0, y10, y20, y30, y40)))

    norma = np.sqrt(
        (ysingle1 - ydouble1) ** 2 + (ysingle2 - ydouble2) ** 2 + (ysingle3 - ydouble3) ** 2 + (
                ysingle4 - ydouble4) ** 2) / (1 - 2 ** (-p))



    print(norma)
    print(rtol * yNorma + atol)

    if (norma>rtol * yNorma + atol):
        acceptArray.append(0)
    else:
        acceptArray.append(1)
    # hn = hn / 2
    # yn11 = y10
    # yn12 = y20
    # yn13 = y30
    # yn14 = y40

    xArray.append(xk)
    hArray.append(h1)

args = xArray
ords = hArray

plt.plot(args, ords, linewidth=2)

for i_x, i_y, accept in zip(args, ords, acceptArray):
    if accept == 1:
        plt.text(i_x, i_y, 'accept')

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
