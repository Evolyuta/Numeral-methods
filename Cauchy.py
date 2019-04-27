# c2 = 0.35
# A = 3
# B = -3
# C = 3
# opponent - 26
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

c2 = 0.35
A = 3
B = -3
C = 3

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

f1 = lambda x, y1, y2, y3, y4: 2 * x * np.power(y2, 1 / B) * y4
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B / C * (y3 - A)) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)

hArray = []
normaArray = []

for k in range(5,11):

    x0 = 0
    xlast = 5
    h = 1 / np.power(2, k)
    hArray.append(h)

    while x0 <= xlast:
        f10 = f1(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f20 = f2(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f30 = f3(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f40 = f4(x0, y1(x0), y2(x0), y3(x0), y4(x0))

        # y11 = y1(x0) + h * f1(x0 + h / 2, y1(x0) + h / 2 * f10, y2(x0) + h / 2 * f10, y3(x0) + h / 2 * f10,
        #                       y4(x0) + h / 2 * f10)
        # y21 = y2(x0) + h * f2(x0 + h / 2, y1(x0) + h / 2 * f20, y2(x0) + h / 2 * f20, y3(x0) + h / 2 * f20,
        #                       y4(x0) + h / 2 * f20)
        # y31 = y3(x0) + h * f3(x0 + h / 2, y1(x0) + h / 2 * f30, y2(x0) + h / 2 * f30, y3(x0) + h / 2 * f30,
        #                       y4(x0) + h / 2 * f30)
        # y41 = y4(x0) + h * f4(x0 + h / 2, y1(x0) + h / 2 * f40, y2(x0) + h / 2 * f40, y3(x0) + h / 2 * f40,
        #                       y4(x0) + h / 2 * f40)

        y11 = y1(x0) + h * (1.43 * f10 + 0.43 * f1(x0 + 0.35 * h, y1(x0) + 0.35 * h * f10, y2(x0) + 0.35 * h * f10,
                                                   y3(x0) + 0.35 * h * f10, y4(x0) + 0.35 * h * f10))
        y21 = y2(x0) + h * (1.43 * f20 + 0.43 * f2(x0 + 0.35 * h, y1(x0) + 0.35 * h * f20, y2(x0) + 0.35 * h * f20,
                                                   y3(x0) + 0.35 * h * f20, y4(x0) + 0.35 * h * f20))
        y31 = y3(x0) + h * (1.43 * f30 + 0.43 * f3(x0 + 0.35 * h, y1(x0) + 0.35 * h * f30, y2(x0) + 0.35 * h * f30,
                                                   y3(x0) + 0.35 * h * f30, y4(x0) + 0.35 * h * f30))
        y41 = y4(x0) + h * (1.43 * f40 + 0.43 * f4(x0 + 0.35 * h, y1(x0) + 0.35 * h * f40, y2(x0) + 0.35 * h * f40,
                                                   y3(x0) + 0.35 * h * f40, y4(x0) + 0.35 * h * f40))

        x0 = x0 + h

    norma = np.sqrt((y1(xlast) - y11) ** 2 + (y2(xlast) - y21) ** 2 + (y3(xlast) - y31) ** 2 + (y4(xlast) - y41) ** 2)
    normaArray.append(norma)
    # print(xlast, y11, y21, y31, y41)
    # print(xlast, y1(xlast), y2(xlast), y3(xlast), y4(xlast))
    print(k)

print(hArray)
print(normaArray)


t = np.linspace(hArray[5],hArray[0])
a = 200*t

args = hArray
ords = normaArray

plt.plot(args, ords, t, a, linewidth=2)
plt.ylabel('Norma')

for i_x, i_y in zip(args, ords):
    # if i_x % 1 == 0:
        plt.text(i_x, i_y, '({}, {})'.format(i_x, '%.2f' % i_y))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
