# c2 = 0.35
# A = 3
# B = -3
# C = 3
# opponent - 26
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# c2 = 0.35
A = 3
B = -3
C = 3
tol = 0.1e-5
p = 2

ycheck1 = lambda x: np.exp(np.sin(x * x))
ycheck2 = lambda x: np.exp(B * np.sin(x * x))
ycheck3 = lambda x: C * np.sin(x * x) + A
ycheck4 = lambda x: np.cos(x * x)

f1 = lambda x, y01, y02, y03, y04: 2 * x * y04 * np.power(y02, (1 / (B)))
f2 = lambda x, y01, y02, y03, y04: 2 * B * x * np.exp(B * (y03-A)/C) * y04
f3 = lambda x, y01, y02, y03, y04: 2 * C * x * y04
f4 = lambda x, y01, y02, y03, y04: -2 * x * np.log((y01))

hArray = []
kArray = []
normaArray = []
halfnormaArray = []
# opnormaArray = []

print(ycheck2(2.5))
n = 2

for k in range(n, n + 1):

    x0 = 0
    xlast = 5
    h = 1 / np.power(2, k)
    hArray.append(h)
    kArray.append(k)

    y1 = ycheck1(x0)
    y2 = ycheck2(x0)
    y3 = ycheck3(x0)
    y4 = ycheck4(x0)

    while x0 <= 2.6953125:
        f10 = f1(x0, y1, y2, y3, y4)
        f20 = f2(x0, y1, y2, y3, y4)
        f30 = f3(x0, y1, y2, y3, y4)
        f40 = f4(x0, y1, y2, y3, y4)
        #
        # y11 = float(y1 + h * (
        #         1.43 * f1(x0, y1, y2, y3, y4) + 0.43 * f1(x0 + 0.35 * h, y1 + 0.35 * h * f1(x0, y1, y2, y3, y4),
        #                                                   y2 + 0.35 * h * f1(x0, y1, y2, y3, y4),
        #                                                   y3 + 0.35 * h * f1(x0, y1, y2, y3, y4),
        #                                                   y4 + 0.35 * h * f1(x0, y1, y2, y3, y4))))
        # y21 = float(y2 + h * (
        #         1.43 * f2(x0, y1, y2, y3, y4) + 0.43 * f2(x0 + 0.35 * h, y1 + 0.35 * h * f2(x0, y1, y2, y3, y4),
        #                                                   y2 + 0.35 * h * f2(x0, y1, y2, y3, y4),
        #                                                   y3 + 0.35 * h * f2(x0, y1, y2, y3, y4),
        #                                                   y4 + 0.35 * h * f2(x0, y1, y2, y3, y4))))
        # y31 = float(y3 + h * (
        #         1.43 * f3(x0, y1, y2, y3, y4) + 0.43 * f3(x0 + 0.35 * h, y1 + 0.35 * h * f3(x0, y1, y2, y3, y4),
        #                                                   y2 + 0.35 * h * f3(x0, y1, y2, y3, y4),
        #                                                   y3 + 0.35 * h * f3(x0, y1, y2, y3, y4),
        #                                                   y4 + 0.35 * h * f3(x0, y1, y2, y3, y4))))
        # y41 = float(y4 + h * (
        #         1.43 * f4(x0, y1, y2, y3, y4) + 0.43 * f4(x0 + 0.35 * h, y1 + 0.35 * h * f4(x0, y1, y2, y3, y4),
        #                                                   y2 + 0.35 * h * f4(x0, y1, y2, y3, y4),
        #                                                   y3 + 0.35 * h * f4(x0, y1, y2, y3, y4),
        #                                                   y4 + 0.35 * h * f4(x0, y1, y2, y3, y4))))

        y11 = ycheck1(x0) + h * f1(x0 + h / 2, y1 + h / 2 * f10, y2 + h / 2 * f10, y3 + h / 2 * f10,
                          y4 + h / 2 * f10)
        y21 = ycheck2(x0) + h * f2(x0 + h / 2, y1 + h / 2 * f20, y2 + h / 2 * f20, y3 + h / 2 * f20,
                          y4 + h / 2 * f20)
        y31 = ycheck3(x0) + h * f3(x0 + h / 2, y1 + h / 2 * f30, y2 + h / 2 * f30, y3 + h / 2 * f30,
                          y4 + h / 2 * f30)
        y41 = ycheck4(x0) + h * f4(x0 + h / 2, y1 + h / 2 * f40, y2 + h / 2 * f40, y3 + h / 2 * f40,
                          y4 + h / 2 * f40)

        y1 = y11
        y2 = y21
        y3 = y31
        y4 = y41
        print(x0, y1, f1(x0 + h / 2, y1 + h / 2 * f10, y2 + h / 2 * f10, y3 + h / 2 * f10,
                          y4 + h / 2 * f10),2 * x0 * (y2 + h / 2 * f10) ** (1 / (B)) *  (y4 + h / 2 * f10))

        x0 = x0 + h

    norma = np.sqrt((y1(xlast) - y11) ** 2 + (y2(xlast) - y21) ** 2 + (y3(xlast) - y31) ** 2 + (y4(xlast) - y41) ** 2)
    normaArray.append(norma)

    print(k)

# print(hArray)
# print(normaArray)

# args = hArray
# ords = normaArray
#
#
#
# plt.plot(args, ords, linewidth=2)
# plt.ylabel('Norma')
#
# for i_x, i_y in zip(args, ords):
#     if i_x % 1 == 0:
# plt.text(i_x, i_y, '({}, {})'.format('%.3f' % i_x, '%.2f' % i_y, ))
#
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
#
# plt.show()
