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

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

f1 = lambda x, y1, y2, y3, y4: 2 * x * np.power(y2, 1 / B) * y4
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B / C * (y3 - A)) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)

hArray = []
kArray = []
normaArray = []
halfnormaArray = []
# opnormaArray = []

for k in range(9, 10):

    x0 = 0
    xlast = 5
    h = 1 / np.power(2, k)
    hArray.append(h)
    kArray.append(k)

    while x0 <= xlast:
        f10 = f1(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f20 = f2(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f30 = f3(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f40 = f4(x0, y1(x0), y2(x0), y3(x0), y4(x0))

        # opy11 = y1(x0) + h * f1(x0 + h / 2, y1(x0) + h / 2 * f10, y2(x0) + h / 2 * f10, y3(x0) + h / 2 * f10,
        #                         y4(x0) + h / 2 * f10)
        # opy21 = y2(x0) + h * f2(x0 + h / 2, y1(x0) + h / 2 * f20, y2(x0) + h / 2 * f20, y3(x0) + h / 2 * f20,
        #                         y4(x0) + h / 2 * f20)
        # opy31 = y3(x0) + h * f3(x0 + h / 2, y1(x0) + h / 2 * f30, y2(x0) + h / 2 * f30, y3(x0) + h / 2 * f30,
        #                         y4(x0) + h / 2 * f30)
        # opy41 = y4(x0) + h * f4(x0 + h / 2, y1(x0) + h / 2 * f40, y2(x0) + h / 2 * f40, y3(x0) + h / 2 * f40,
        #                         y4(x0) + h / 2 * f40)

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

    x0 = 0
    h = h / 2

    while x0 <= xlast:
        f10 = f1(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f20 = f2(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f30 = f3(x0, y1(x0), y2(x0), y3(x0), y4(x0))
        f40 = f4(x0, y1(x0), y2(x0), y3(x0), y4(x0))

        # opy11 = y1(x0) + h * f1(x0 + h / 2, y1(x0) + h / 2 * f10, y2(x0) + h / 2 * f10, y3(x0) + h / 2 * f10,
        #                         y4(x0) + h / 2 * f10)
        # opy21 = y2(x0) + h * f2(x0 + h / 2, y1(x0) + h / 2 * f20, y2(x0) + h / 2 * f20, y3(x0) + h / 2 * f20,
        #                         y4(x0) + h / 2 * f20)
        # opy31 = y3(x0) + h * f3(x0 + h / 2, y1(x0) + h / 2 * f30, y2(x0) + h / 2 * f30, y3(x0) + h / 2 * f30,
        #                         y4(x0) + h / 2 * f30)
        # opy41 = y4(x0) + h * f4(x0 + h / 2, y1(x0) + h / 2 * f40, y2(x0) + h / 2 * f40, y3(x0) + h / 2 * f40,
        #                         y4(x0) + h / 2 * f40)

        halfy11 = y1(x0) + h * (1.43 * f10 + 0.43 * f1(x0 + 0.35 * h, y1(x0) + 0.35 * h * f10, y2(x0) + 0.35 * h * f10,
                                                       y3(x0) + 0.35 * h * f10, y4(x0) + 0.35 * h * f10))
        halfy21 = y2(x0) + h * (1.43 * f20 + 0.43 * f2(x0 + 0.35 * h, y1(x0) + 0.35 * h * f20, y2(x0) + 0.35 * h * f20,
                                                       y3(x0) + 0.35 * h * f20, y4(x0) + 0.35 * h * f20))
        halfy31 = y3(x0) + h * (1.43 * f30 + 0.43 * f3(x0 + 0.35 * h, y1(x0) + 0.35 * h * f30, y2(x0) + 0.35 * h * f30,
                                                       y3(x0) + 0.35 * h * f30, y4(x0) + 0.35 * h * f30))
        halfy41 = y4(x0) + h * (1.43 * f40 + 0.43 * f4(x0 + 0.35 * h, y1(x0) + 0.35 * h * f40, y2(x0) + 0.35 * h * f40,
                                                       y3(x0) + 0.35 * h * f40, y4(x0) + 0.35 * h * f40))

        x0 = x0 + h

    # halfnorma = np.sqrt((y1(xlast) - y11) ** 2 + (y2(xlast) - y21) ** 2 + (y3(xlast) - y31) ** 2 + (y4(xlast) - y41) ** 2)
    # halfnormaArray.append(halfnorma)

    # opnorma = np.sqrt(
    #     (y1(xlast) - opy11) ** 2 + (y2(xlast) - opy21) ** 2 + (y3(xlast) - opy31) ** 2 + (y4(xlast) - opy41) ** 2)
    # opnormaArray.append(opnorma)
    print(k)

print(hArray)
print(normaArray)
# print(halfnormaArray)
# print(opnormaArray)


args = hArray
ords = normaArray

# ords1 = opnormaArray

# tarray = []
# tfirst = normaArray[0]
# while tfirst >= normaArray[-1]:
#     tarray.append(tfirst)
#     tfirst = tfirst / 2
# tarray.append(normaArray[-1])
#
# plt.plot(args, ords, args, tarray, linewidth=2)
# plt.ylabel('Norma')
#
# for i_x, i_y in zip(args, ords):
#     # if i_x % 1 == 0:
#     plt.text(i_x, i_y, '({}, {})'.format('%.3f' % i_x, '%.2f' % i_y, ))
#
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
#
# plt.show()

halfnorma = np.sqrt((halfy11 - y11) ** 2 + (halfy21 - y21) ** 2 + (halfy31 - y31) ** 2 + (halfy41 - y41) ** 2)

R2n = (halfnorma / (2 ** p - 1))
print(R2n)
htol = h * np.power((tol / abs(R2n)), 1 / p)
print(htol)

normaArray = []

x0 = 0
xArray = []
xlast = 5
h = htol

while x0 <= xlast:
    f10 = f1(x0, y1(x0), y2(x0), y3(x0), y4(x0))
    f20 = f2(x0, y1(x0), y2(x0), y3(x0), y4(x0))
    f30 = f3(x0, y1(x0), y2(x0), y3(x0), y4(x0))
    f40 = f4(x0, y1(x0), y2(x0), y3(x0), y4(x0))

    # opy11 = y1(x0) + h * f1(x0 + h / 2, y1(x0) + h / 2 * f10, y2(x0) + h / 2 * f10, y3(x0) + h / 2 * f10,
    #                         y4(x0) + h / 2 * f10)
    # opy21 = y2(x0) + h * f2(x0 + h / 2, y1(x0) + h / 2 * f20, y2(x0) + h / 2 * f20, y3(x0) + h / 2 * f20,
    #                         y4(x0) + h / 2 * f20)
    # opy31 = y3(x0) + h * f3(x0 + h / 2, y1(x0) + h / 2 * f30, y2(x0) + h / 2 * f30, y3(x0) + h / 2 * f30,
    #                         y4(x0) + h / 2 * f30)
    # opy41 = y4(x0) + h * f4(x0 + h / 2, y1(x0) + h / 2 * f40, y2(x0) + h / 2 * f40, y3(x0) + h / 2 * f40,
    #                         y4(x0) + h / 2 * f40)

    y11 = y1(x0) + h * (1.43 * f10 + 0.43 * f1(x0 + 0.35 * h, y1(x0) + 0.35 * h * f10, y2(x0) + 0.35 * h * f10,
                                               y3(x0) + 0.35 * h * f10, y4(x0) + 0.35 * h * f10))
    y21 = y2(x0) + h * (1.43 * f20 + 0.43 * f2(x0 + 0.35 * h, y1(x0) + 0.35 * h * f20, y2(x0) + 0.35 * h * f20,
                                               y3(x0) + 0.35 * h * f20, y4(x0) + 0.35 * h * f20))
    y31 = y3(x0) + h * (1.43 * f30 + 0.43 * f3(x0 + 0.35 * h, y1(x0) + 0.35 * h * f30, y2(x0) + 0.35 * h * f30,
                                               y3(x0) + 0.35 * h * f30, y4(x0) + 0.35 * h * f30))
    y41 = y4(x0) + h * (1.43 * f40 + 0.43 * f4(x0 + 0.35 * h, y1(x0) + 0.35 * h * f40, y2(x0) + 0.35 * h * f40,
                                               y3(x0) + 0.35 * h * f40, y4(x0) + 0.35 * h * f40))


    norma = np.sqrt((y1(x0) - y11) ** 2 + (y2(x0) - y21) ** 2 + (y3(x0) - y31) ** 2 + (y4(x0) - y41) ** 2)
    normaArray.append(norma)
    print('x0 = %.3f' %x0, ' norma = %.10f' %norma)
    xArray.append(x0)
    x0 = x0 + h

args = xArray
ords = normaArray

plt.plot(args, ords, linewidth=2)
plt.ylabel('Norma')

# for i_x, i_y in zip(args, ords):
#     if i_x % 1 == 0:
# plt.text(i_x, i_y, '({}, {})'.format('%.3f' % i_x, '%.2f' % i_y, ))

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()