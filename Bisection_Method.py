from math import *
import math

## Bisection Method

def bisection_method(a, b, eps, f):
    fa = f(a)
    fb = f(b)
    if f(a)*f(b) > 0 :
        return
    n = (math.log(b-a) - math.log(eps))/(math.log(2))
    n = int(n)
    for i in range(n):
        #print "in loop"
        c = a + 0.5*(b-a)
        fc = f(c)
        if fa*fc < 0:
            b = c
            fb = fc
        elif fa*fc > 0:
            a = c
            fa = fc
        else:
            a = c
    return a

## Question 1 - Exercise 3, 6, 7 (page 95), 3 (page 104)
print
print "Question 1"
def a(x):
    return (x**3) - 2
print "a:",bisection_method(0,2,0.000001, a)

def b(x):
    return math.exp(x) - 2
print "b:", bisection_method(0,1,0.000001,b)

def c(x):
    return x - math.exp(-x)
print "c:", bisection_method(0,1,0.000001,c)

def d(x):
    return x**6 - x - 1
print "d:", bisection_method(0,2,0.000001,d)

def e(x):
    return x**3 - 2*x - 5
print "e:", bisection_method(0,3,0.000001,e)

def f(x):
    return 1 - 2*x*math.exp(-x/2)
print "f:", bisection_method(0,2,0.000001,f)

def g(x):
    return 5 - x**(-1)
print "g:", bisection_method(0.1,0.25,0.000001,g)

def h(x):
    return x*x - math.sin(x)
print "h:", bisection_method(0.1,math.pi,0.000001,h)

#### Question 2 - Exercise 8 from page 106
print
print "Question 2"

def annuity_equation(x):
    return 15 - ((0.72)/x)*(1-(((12+x)/12)**(-255)*((12+x)/12)**(-105)))
print "r =", bisection_method(0.01,0.04,0.000001,annuity_equation)


#### Question 3 - Exercise 9 from page 106
print
print "Question 3"
def annuity_equation1(x):
    return 10 - ((0.72)/x)*(1-(((12+x)/12)**(-255)*((12+x)/12)**(-105)))
print "r =", bisection_method(0.05,0.07,0.000001,annuity_equation1)

