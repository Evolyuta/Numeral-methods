import sympy as sympy
from numpy import linalg
import scipy.integrate as spint
from sympy import *
from sympy.matrices import *
import numpy as np

x = Symbol("x")

a=-1.0
b=1.0
step=0.5
xpoint = a
xarray = []
yarray = []

while (xpoint<=b):
    xarray.append(xpoint)
    yarray.append(3*xpoint-cos(xpoint-1))
    xpoint=xpoint+step

mnkx = np.zeros((4, 4))
mnkx[0][0]=5

#sumx=sum(xarray)

xsqarray = []
xcoarray = []
xfoarray = []
xfiarray = []
xsiarray = []
for xpoint in xarray:
    xsqarray.append(xpoint*xpoint)
    xcoarray.append(xpoint*xpoint*xpoint)
    xfoarray.append(xpoint*xpoint*xpoint*xpoint)
    xfiarray.append(xpoint*xpoint*xpoint*xpoint*xpoint)
    xsiarray.append(xpoint*xpoint*xpoint*xpoint*xpoint*xpoint)

sumx=sum(xarray)
sumsqx=sum(xsqarray)
sumcox=sum(xcoarray)
sumfox=sum(xfoarray)
sumfix=sum(xfiarray)
sumsix=sum(xsiarray)

mnkx [0][1] = sumx
mnkx [1][0] = sumx

mnkx [0][2] = sumsqx
mnkx [1][1] = sumsqx
mnkx [2][0] = sumsqx

mnkx [0][3] = sumcox
mnkx [1][2] = sumcox
mnkx [2][1] = sumcox
mnkx [3][0] = sumcox

mnkx [1][3] = sumfox
mnkx [2][2] = sumfox
mnkx [3][1] = sumfox

mnkx [2][3] = sumfix
mnkx [3][2] = sumfix

mnkx [3][3] = sumsix

xyarray=[]
xsqyarray=[]
xcoyarray=[]
for i in range(5):
    xyarray.append(xarray[i]*yarray[i])
    xsqyarray.append(xarray[i]*xarray[i]*yarray[i])
    xcoyarray.append(xarray[i]*xarray[i]*xarray[i]*yarray[i])

sumy=sum(yarray)
sumxy=sum(xyarray)
sumsqxy=sum(xsqyarray)
sumcoxy=sum(xcoyarray)

mnky = np.zeros((4, 1))
mnky[0][0]=sumy
mnky[1][0]=sumxy
mnky[2][0]=sumsqxy
mnky[3][0]=sumcoxy

resmatrix=np.dot(linalg.inv(mnkx), mnky)

res=resmatrix[0][0]+resmatrix[1][0]*x+resmatrix[2][0]*x*x+resmatrix[3][0]*x*x*x





L=1
P1=x
P2=cancel((3*x*x-1)/2)
P3=cancel((5*x*x*x-3*x)/2)

def P0(t):
    return 1

def P1(t):
    return t

def P2(t):
    return (3*t*t-1)/2

def P3(t):
    return (5*t*t*t-3*t)/2


A = np.zeros((4, 4))

A[0][0] = P0(xarray[0])
A[0][1] = P1(xarray[0])
A[0][2] = P2(xarray[0])
A[0][3] = P3(xarray[0])

A[1][0] = P0(xarray[1])
A[1][1] = P1(xarray[1])
A[1][2] = P2(xarray[1])
A[1][3] = P3(xarray[1])

A[2][0] = P0(xarray[2])
A[2][1] = P1(xarray[2])
A[2][2] = P2(xarray[2])
A[2][3] = P3(xarray[2])

A[3][0] = P0(xarray[3])
A[3][1] = P1(xarray[3])
A[3][2] = P2(xarray[3])
A[3][3] = P3(xarray[3])

B = np.zeros((4, 1))

B[0][0] = yarray[0]
B[1][0] = yarray[1]
B[2][0] = yarray[2]
B[3][0] = yarray[3]

resmatrix1=np.dot(linalg.inv(A), B)

res1=resmatrix[0][0]+resmatrix[1][0]*x+resmatrix[2][0]*x*x+resmatrix[3][0]*x*x*x



fx=3*x-cos(x-1)

"""p = plot(fx, (x, -1, 1))
p = plot(res, (x, -1, 1))
p = plot(res1, (x, -1, 1))"""

p = plot(res,(x, -1, 1))
p = plot( res1,(x, -1, 1))
p = plot(fx, (x, -1, 1))