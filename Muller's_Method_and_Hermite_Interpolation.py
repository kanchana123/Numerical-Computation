from math import *
from matplotlib import pyplot

##### Mullers's Method #####

def b(xn, xn2, xn1, f):
    return (1.0/(xn - xn2))*(((f(xn)-f(xn1))/(xn-xn1)) - ((f(xn1)-f(xn2))/(xn1 - xn2)))

def c(f, xn, xn1, b):
    return ((f(xn)-f(xn1))/(xn - xn1)) + b*(xn - xn1)

def x(xn, f, c, b):
    sign = c/abs(c)
    return (xn - ((2.0 * f(xn))/(c + sign*(((c*c) - 4.0*f(xn)*b)**0.5))))

print 'Question 1'

def f1(x):
    return 2 - exp(x)

x0 = 0.0 # xn2
x1 = 0.5 # xn1
x2 = 1.0 # xn

for i in range(3):
    bn = b(x2, x0, x1, f1)
    cn = c(f1, x2, x1, bn)
    xn = x(x2, f1, cn, bn)
    
    x0 = x1
    x1 = x2
    x2 = xn
    print 'x',i+3, '=', xn

print
print 'Question 2'
def f2(x):
    return (x**6) - x - 1

x0 = 0.0 # xn2
x1 = 1.0 # xn1
x2 = 2.0 # xn

for i in range(3):
    bn = b(x2, x0, x1, f2)
    cn = c(f2, x2, x1, bn)
    xn = x(x2, f2, cn, bn)
    
    x0 = x1
    x1 = x2
    x2 = xn
    print 'x',i+3, '=', xn

#### Hermite Interpolation ######
print
print 'Question 3'
def f3(x):
    return sin(x)

def h1(x):
    return (-1.0/pi)*x*x + x

x_plot = [i/100.0 for i in range(315)]

pyplot.figure(1)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,map(f3,x_plot))
pyplot.plot(x_plot,map(h1,x_plot))
pyplot.show()
print 'Figure 1'

print
print 'Question 4'
def f4(x):
    return (1 + x)**0.5

def h2(x):
    return 1.0 + (0.5)*x + ((2*(2**0.5) - 3)/2)*x*x + ((10 - 7.0*(2**0.5))/4)*(x**3-x*x)

x_plot = [i/100.0 for i in range(101)]

pyplot.figure(2)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,map(f4,x_plot))
pyplot.plot(x_plot,map(h2,x_plot))
print 'Figure 2'
