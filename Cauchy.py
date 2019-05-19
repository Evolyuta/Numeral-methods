import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

A = 3
B = 1
C = 3
c2 = 0.35
b2 = 1 / (2 * c2)
b1 = 1 - b2

x0 = 0
xn = 5

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

y10 = y1(0)
y20 = y2(0)
y30 = y3(0)
y40 = y4(0)

hArray = []
normaArray = []
opnormaArray = []

f1 = lambda x, y1, y2, y3, y4: 2 * x * y4 * y2 ** (1 / B)
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B * (y3 - A) / C) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)

for k in range(9, 13):

    x0 = 0
    y10 = y1(0)
    y20 = y2(0)
    y30 = y3(0)
    y40 = y4(0)
    h = 1 / np.power(2, k)
    hArray.append(h)

    while x0 < 5:
        # y11 = y10 + h * f1(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y21 = y20 + h * f2(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y31 = y30 + h * f3(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y41 = y40 + h * f4(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))

        # y11 = y10 + h * (1.43 * f1(x0, y10, y20, y30, y40) +
        #                  0.43 * f1(x0 + 0.35 * h,
        #                            y10 + 0.35 * h * f1(x0, y10, y20, y30, y40),
        #                            y20 + 0.35 * h * f2(x0, y10, y20, y30, y40),
        #                            y30 + 0.35 * h * f3(x0, y10, y20, y30, y40),
        #                            y40 + 0.35 * h * f4(x0, y10, y20, y30, y40)))
        # y21 = y20 + h * (1.43 * f2(x0, y10, y20, y30, y40) +
        #                  0.43 * f2(x0 + 0.35 * h,
        #                            y10 + 0.35 * h * f1(x0, y10, y20, y30, y40),
        #                            y20 + 0.35 * h * f2(x0, y10, y20, y30, y40),
        #                            y30 + 0.35 * h * f3(x0, y10, y20, y30, y40),
        #                            y40 + 0.35 * h * f4(x0, y10, y20, y30, y40)))
        # y31 = y30 + h * (1.43 * f3(x0, y10, y20, y30, y40) +
        #                  0.43 * f3(x0 + 0.35 * h,
        #                            y10 + 0.35 * h * f1(x0, y10, y20, y30, y40),
        #                            y20 + 0.35 * h * f2(x0, y10, y20, y30, y40),
        #                            y30 + 0.35 * h * f3(x0, y10, y20, y30, y40),
        #                            y40 + 0.35 * h * f4(x0, y10, y20, y30, y40)))
        # y41 = y40 + h * (1.43 * f4(x0, y10, y20, y30, y40) +
        #                  0.43 * f4(x0 + 0.35 * h,
        #                            y10 + 0.35 * h * f1(x0, y10, y20, y30, y40),
        #                            y20 + 0.35 * h * f2(x0, y10, y20, y30, y40),
        #                            y30 + 0.35 * h * f3(x0, y10, y20, y30, y40),
        #                            y40 + 0.35 * h * f4(x0, y10, y20, y30, y40)))

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

    norma = np.sqrt((y1(xn) - y11) ** 2 + (y2(xn) - y21) ** 2 + (y3(xn) - y31) ** 2 + (y4(xn) - y41) ** 2)
    normaArray.append(norma)

hArray = []
c2 = 0.5
b2 = 1 / (2 * c2)
b1 = 1 - b2

for k in range(9,13):

    x0 = 0
    y10 = y1(0)
    y20 = y2(0)
    y30 = y3(0)
    y40 = y4(0)
    h = 1 / np.power(2, k)
    hArray.append(h)

    while x0 < 5:
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

        # y11 = y10 + h * f1(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y21 = y20 + h * f2(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y31 = y30 + h * f3(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))
        # y41 = y40 + h * f4(x0 + h / 2,
        #                    y10 + h / 2 * f1(x0, y10, y20, y30, y40),
        #                    y20 + h / 2 * f2(x0, y10, y20, y30, y40),
        #                    y30 + h / 2 * f3(x0, y10, y20, y30, y40),
        #                    y40 + h / 2 * f4(x0, y10, y20, y30, y40))

        y10 = y11
        y20 = y21
        y30 = y31
        y40 = y41

        x0 = x0 + h

    norma = np.sqrt((y1(xn) - y11) ** 2 + (y2(xn) - y21) ** 2 + (y3(xn) - y31) ** 2 + (y4(xn) - y41) ** 2)
    opnormaArray.append(norma)

print(hArray)
print(normaArray)
print(opnormaArray)

args = hArray
ords = normaArray

tarray = []
tfirst = (normaArray[0] + opnormaArray[0]) / 2
while len(tarray) != len(normaArray):
    tarray.append(tfirst)
    tfirst = tfirst / 2
# tarray.append(normaArray[-1])

print((tarray))

plt.plot(args, ords, 'g', args, opnormaArray, 'b', args, tarray, 'r', linewidth=2)
plt.ylabel('Norma')

# for i_x, i_y in zip(args, ords):
# if i_x % 1 == 0:
# plt.text(i_x, i_y, '({}, {})'.format('%.4f' % i_x, '%.4f' % i_y, ))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()