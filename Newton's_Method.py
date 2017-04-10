from math import *
from matplotlib import pyplot

## Netwon's Method
def f(x):
    return x*x - 2

def fn(x):
    return abs((x-2**(0.5)))

def fn1(x):
    f_x = x*x - 2
    f2_x = 2 * x
    return abs((x - f_x/f2_x)-2**(0.5))

x = [i/10.0 for i in range(1,51)]

sqrt_c = float(2**(0.5))

pyplot.ion()
pyplot.clf()
pyplot.plot(x, map(f,x))
pyplot.plot(x,map(fn,x))
pyplot.plot(x, map(fn1, x))
