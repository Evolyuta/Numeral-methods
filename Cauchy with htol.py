import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

A = 3
B = 1
C = 3

tol = 1e-5
p = 2

c2 = 0.35
b2 = 1 / (2 * c2)
b1 = 1 - b2

# x0 = 0
xn = 5

y1 = lambda x: np.exp(np.sin(x * x))
y2 = lambda x: np.exp(B * np.sin(x * x))
y3 = lambda x: C * np.sin(x * x) + A
y4 = lambda x: np.cos(x * x)

f1 = lambda x, y1, y2, y3, y4: 2 * x * y4 * y2 ** (1 / B)
f2 = lambda x, y1, y2, y3, y4: 2 * B * x * np.exp(B * (y3 - A) / C) * y4
f3 = lambda x, y1, y2, y3, y4: 2 * C * x * y4
f4 = lambda x, y1, y2, y3, y4: -2 * x * np.log(y1)

htol= 1.9373350415596262e-06
x0 = 0
y10 = y1(0)
y20 = y2(0)
y30 = y3(0)
y40 = y4(0)

xArray = []

h = htol
normaArray = []
while x0 < xn:
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

    norma = np.sqrt((y1(x0) - y11) ** 2 + (y2(x0) - y21) ** 2 + (y3(x0) - y31) ** 2 + (y4(x0) - y41) ** 2)

    xArray.append(x0)
    normaArray.append(norma)
    print(x0)


    y10 = y11
    y20 = y21
    y30 = y31
    y40 = y41

    x0 = x0 + h

norma = np.sqrt((y1(xn) - y11) ** 2 + (y2(xn) - y21) ** 2 + (y3(xn) - y31) ** 2 + (y4(xn) - y41) ** 2)
print(norma)

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