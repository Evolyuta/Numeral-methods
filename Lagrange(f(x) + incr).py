from sympy import *
from sympy.matrices import *
import numpy as np

x = Symbol("x")

for n in [3,6,9,12]:
    a=-10.0
    b=10.0
    step=abs(b-a)/(n)
    xpoint = a
    xarray = []
    yarray = []

    while (xpoint<=b):
        xarray.append(xpoint)
        yarray.append(3*xpoint-cos(xpoint)-1)
        #yarray.append(tan(xpoint))
        xpoint=xpoint+step

    xlast = xarray[n - 1]

    p=0
    i=0

    for ypoint in yarray:
        ppoint=ypoint
        for xpoint in xarray:
            if (xpoint!=xarray[i]):
                ppoint*=(x-xpoint)/(xarray[i]-xpoint)
        p=p+ppoint
        i=i+1


    print('a = ', a)
    print('b = ', b)
    print('n = ', n)
    print('xpoints = ', xarray)
    print('ypoints = ', yarray)
    print('Lagrange Polynomial: ',cancel(p))

#print(p.evalf(subs={x:10}))

    xarray = []
    yarray = []
    for i in range(n+1):
        xpoint=0.5*((b-a)*cos(np.pi*(2*i+1)/(2*(n+1)))+(b+a))
        xarray.append(xpoint)
        yarray.append(3 * xpoint - cos(xpoint) - 1)

    xfirst = xarray[n - 1]


    cp=0
    i=0

    for ypoint in yarray:
        ppoint=ypoint
        for xpoint in xarray:
            if (xpoint!=xarray[i]):
                ppoint*=(x-xpoint)/(xarray[i]-xpoint)
        cp=cp+ppoint
        i=i+1

    print('Chebyshev xpoints = ', xarray)
    print('Chebyshev ypoints = ', yarray)
    print('Chebyshev Lagrange Polynomial: ', cancel(cp), '\n\n')

    p = plot(p, cp, (x, -1, 1), title='3x-cos(x)-1 ('+str(n)+' points)', show=false)
    p[1].line_color = 'r'

    p.show()