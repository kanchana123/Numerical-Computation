from math import *

def trapezoid(f, a, b, n):
    a, b = float(a), float(b)
    h = (b - a)/n
    s = f(a) + f(b)
    x = a
    for i in range(n-1):
        x = x + h
        s = s + 2*f(x)
    s = s*(h/2.0)
    return s

def trapezoid_c(t, fp, a, b, n):
    a, b = float(a), float(b)
    h = (b - a)/n
    t_c = t - (h*h*(fp(b)-fp(a))/12.0)
    return t_c

def display_table(value, f, fp, a, b):
    ratio = 0
    prev_err = 0
    print 'n    |    t         |  tc          |       error        | ratio'
    for i in range(1,12):
        n = 2**i
        t = trapezoid(f, a, b, n)
        tc = trapezoid_c(t,fp,a,b,n)
        error = value - tc
        if i > 1 and error != 0:
            ratio = prev_err/error
        print '%.4d | %.10f | %.10f |' % (n, t, tc), error, ' | %.4f' % ( ratio)
        prev_err = error

print 'Q. 1'
t = trapezoid(lambda x: x - x**3 , 0, 1, 4)
print 'Trapezoid Rule:', t
print 'Corrected Trapezoid Rule:', trapezoid_c(t, lambda x: 1 - 3*x*x, 0, 1, 4)

print
print 'Q. 2'
t = trapezoid(lambda x: 1.0/((1+x**4)**0.5) , 0, 1, 4)
print 'Trapezoid Rule:', t
print 'Corrected Trapezoid Rule:', trapezoid_c(t, lambda x: (-4*(x**3)*(1+x**4)**(-0.5))/(2+2*x**4), 0, 1, 4)

print
print 'Q. 3'
t = trapezoid(lambda x: log(1+x) ,0,1,4)
print 'Trapezoid Rule:', t
print 'Corrected Trapezoid Rule:', trapezoid_c(t, lambda x: 1/(1+x), 0, 1, 4)

print
print 'Q. 4'
t = trapezoid(lambda x: 1/(1+x**3) ,0,1,4)
print 'Trapezoid Rule:', t
print 'Corrected Trapezoid Rule:', trapezoid_c(t, lambda x: -3*x*x/(1+x**3)**2, 0, 1, 4)

print
print 'Q. 5'
t = trapezoid(lambda x: exp(-(x*x)) ,1,2,4)
t_c = trapezoid_c(t, lambda x: -2*x*exp(-(x*x)), 1, 2, 4)
print 'Trapezoid Rule:', t
print 'Corrected Trapezoid Rule:', t_c

print
print 'Question 6'
print "a. "
display_table(2-10*exp(-2), lambda x: x*x*exp(-x), lambda x: 2*x*exp(-x) - \
              x*x*exp(-x), 0, 2)

print
print "b. "
display_table(2.0*atan(5.0), lambda x: 1/(1+(x*x)), lambda x: -2*x/((1+(x*x))**2), -5, 5)

print
print "c. "
display_table(3*log(3) - 2, lambda x: log(x), lambda x: 1/x, 1, 3)

print
print "d. "
display_table((4.0/17)*(1-exp(-pi)), lambda x: exp(-x)*sin(4*x), \
              lambda x: -exp(-x)*sin(4*x) + 4*cos(4*x)*exp(-x), 0,pi)

print
print "e. "
t = trapezoid(lambda x: (1 - x*x)**0.5, -1,1,2048)
print t
print "Zero devision error when calculating the corrected trapezoid approximation."
#display_table(pi/2, lambda x: (1 - x*x)**0.5, lambda x: -2*x*0.5/(1-x*x)**(0.5), -1, 1)

print
print 'Question 7'
display_table(0.0808308960, lambda x: x*x*exp(-2*x), lambda x: 2*x*exp(-2*x) - 2*x*x*exp(-2*x), 0, 1)

print "The error becomes 0 because f'(1) - f'(0) = 0. \
Therefore, the result from trapezoid rule and corrected trapezoid rule are same."

print
print 'Question 8'
display_table(0.5*pi, lambda x: (sin(x))**2, lambda x: 2*sin(x)*cos(x), 0, pi)
print "The error becomes 0 because f'(pi) = f'(0) = 0. \
Therefore, the result from trapezoid rule and corrected trapezoid rule are same."
