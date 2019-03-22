from sympy import *
from sympy.matrices import *
import numpy as np
from sympy.plotting import plot

x = Symbol("x")
y = Symbol("y")

x1=-1
x2=0
x3=1
y1=-1
y2=0
y3=1

f11=2
f12=2
f13=2
f21=1
f22=0
f23=1
f31=4
f32=2
f33=4


l11=(x-x2)*(x-x3)*(y-y2)*(y-y3)/((x1-x2)*(x1-x3)*(y1-y2)*(y1-y3))
l12=(x-x2)*(x-x3)*(y-y1)*(y-y3)/((x1-x2)*(x1-x3)*(y2-y1)*(y2-y3))
l13=(x-x2)*(x-x3)*(y-y1)*(y-y2)/((x1-x2)*(x1-x3)*(y3-y1)*(y3-y2))
l23=(x-x1)*(x-x3)*(y-y1)*(y-y2)/((x2-x1)*(x2-x3)*(y3-y1)*(y3-y2))
l33=(x-x1)*(x-x2)*(y-y1)*(y-y2)/((x3-x1)*(x3-x2)*(y3-y1)*(y3-y2))
l32=(x-x1)*(x-x2)*(y-y1)*(y-y3)/((x3-x1)*(x3-x2)*(y2-y3)*(y2-y1))
l31=(x-x1)*(x-x2)*(y-y2)*(y-y3)/((x3-x1)*(x3-x2)*(y1-y3)*(y1-y2))
l21=(x-x1)*(x-x3)*(y-y2)*(y-y3)/((x2-x1)*(x2-x3)*(y1-y3)*(y1-y2))
l22=(x-x1)*(x-x3)*(y-y1)*(y-y3)/((x2-x1)*(x2-x3)*(y2-y3)*(y2-y1))

f=f11*l11+f12*l12+f13*l13+f21*l21+f22*l22+f23*l23+f31*l31+f32*l32+f33*l33

print(cancel(f))