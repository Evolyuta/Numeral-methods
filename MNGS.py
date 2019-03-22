import numpy as np

def f(x,y,z):
    return 2*x*x+3.7*y*y+4.7*z*z+x*y-y*z+x*z+x-2*y+3*z+7

a = np.matrix('2 0.5 -0.5; '
              '0.5 3.7 0.5;'
              '-0.5 0.5 4.7')
b = np.matrix('1; -2; 3')

delta = 4.7 - 0.5-0.5-0.5-0.5-0.5-0.5

k=1
x1 = np.matrix('-0.5;0.54;-0.64')
fx1=f(x1.item(0,0),x1.item(1,0),x1.item(2,0))

q1 = a*x1 + b
mu1 = -((q1.transpose())*q1)/(q1.transpose()*(a*q1))
print('\n',k,')\n x = (',x1.item(0,0),',',x1.item(1,0),',',x1.item(2,0),');',
      '\n f(x) =',fx1,';\n q = (',q1.item(0,0),',',q1.item(1,0),',',q1.item(1,0),
      ');\n mu =', mu1.item((0, 0)),';')
k=k+1
x2 = x1 + mu1.item((0, 0))*q1
fx2=f(x2.item(0,0),x2.item(1,0),x2.item(2,0))

grad = a*x2 + b
eps = (np.sqrt(np.square(grad.item(0,0))+np.square(grad.item(1,0))+np.square(grad.item(2,0))))/delta

while (eps>0.000001):
    x1=x2
    fx1=fx2
    q1 = a * x1 + b
    mu1 = -((q1.transpose()) * q1) / (q1.transpose() * (a * q1))
    x2 = x1 + mu1.item((0, 0)) * q1
    fx2 = f(x2.item(0, 0), x2.item(1, 0), x2.item(2, 0))
    grad = a * x2 + b
    eps = (np.sqrt(np.square(grad.item(0, 0)) + np.square(grad.item(1, 0)) + np.square(grad.item(2, 0)))) / delta
    print('\n',k, ')\n x = (', x1.item(0, 0), ',', x1.item(1, 0), ',', x1.item(2, 0), ');',
          '\n f(x) =', fx1, ';\n q = (', q1.item(0, 0), ',', q1.item(1, 0), ',', q1.item(2, 0),
          ');\n mu =', mu1.item((0, 0)), ';\n eps =',eps)
    k = k + 1

