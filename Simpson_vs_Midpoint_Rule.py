from math import *

def simpson(f, a, b, n):
    h = float(b - a) / n
    x = [a + h * i for i in range(n+1)]
    y = map(f,x)
    return (h/3) * (y[0] + 4*sum(y[1::2]) + 2*sum(y[2:-1:2]) + y[-1])

print simpson(lambda x: log(1+x), 0, 1, 4)
result = 2*log(2) - 1

s2 = simpson(lambda x: log(1+x), 0, 1, 4)
print '10^-3   ', s2, 'Error: %.10f' % (result - s2)
s14 = simpson(lambda x: log(1+x), 0, 1, 14)
print '10^-6   ', s14, 'Error: %.10f' % (result - s14)


def display_table(value, f, a, b):
    ratio = 0
    prev_err = 0
    print 'n    |    s         |       error        | ratio'
    for i in range(1,12):
        n = 2**i
        s = simpson(f, a, b, n)
        error = value - s
        if i > 1 and error != 0:
            ratio = prev_err/error
        print '%.4d | %.10f |' % (n, s), error, ' | %.4f' % (ratio)
        prev_err = error

print '\n6a'
display_table(3*log(3) - 2, lambda x: log(x), 1, 3)

print '\n6b'
display_table(2-10*exp(-2), lambda x: x*x*exp(-x), 0, 2)

print '\n6c'
display_table(2.0*atan(5.0), lambda x: 1/(1+(x*x)), -5, 5)

print '\n6d'
display_table(pi/2, lambda x: (1 - x*x)**0.5, -1, 1)

print '\n6e'
display_table((4.0/17)*(1-exp(-pi)), lambda x: exp(-x)*sin(4*x), 0, pi)

print '\nFor (c), the error ratio has big difference but the answers are correct.\
For (d), there is not much decrease in error. Error ratio is increasing very slowly.'

print'\nQuestion 3'
s_pi = 2*simpson(lambda x: (1 - x*x)**0.5, -1, 1, 2048)
print 'pi =', s_pi, 'error = %.10f'%(pi - s_pi)
print "Simpson's rule gives good approximation of pi."

print '\nQuestion 4'

print'\nQuestion 5'

def midpoint(f, a, b, n):
    a, b = float(a), float(b)
    h = (b-a)/n
    s = 0
    for i in range(1,n+1):
        ci = a + (i - (0.5))*h
        s = s + f(ci)
    return s*h

result = 0.25
print midpoint(lambda x: x*(1-x*x), 0, 1, 4)
m16 = midpoint(lambda x: x*(1-x*x), 0, 1, 16)
print '10^-3   ', m16, 'n = 16 error =', abs(result - m16)
m501 = midpoint(lambda x: x*(1-x*x), 0, 1, 501)
print '10^-6   ', m501, 'n = 501  error =', abs(result - m501)

print'\nQuestion 6'
result = 2*log(2) - 1
print midpoint(lambda x: log(1+x), 0, 1, 4)
m7 = midpoint(lambda x: log(1+x), 0, 1, 7)
print '10^-3   ', m7, 'n = 7 Error =', result - m7
m205 = midpoint(lambda x: log(1+x), 0, 1, 205)
print '10^-6   ', m205, 'n = 7 Error =', result - m205

print'\nQuestion 7'

def display_table(value, f, a, b):
    ratio = 0
    prev_err = 0
    print 'n    |    m         |       error        | ratio'
    for i in range(1,12):
        n = 2**i
        m = midpoint(f, a, b, n)
        error = value - m
        if i > 1 and error != 0:
            ratio = prev_err/error
        print '%.4d | %.10f |' % (n, m), error, ' | %.4f' % (ratio)
        prev_err = error

print '\n7a'
display_table(3*log(3) - 2, lambda x: log(x), 1, 3)

print '\n7b'
display_table(2-10*exp(-2), lambda x: x*x*exp(-x), 0, 2)

print '\n7c'
display_table(2.0*atan(5.0), lambda x: 1/(1+(x*x)), -5, 5)

print '\n7d'
display_table(pi/2, lambda x: (1 - x*x)**0.5, -1, 1)

print '\n7e'
display_table((4.0/17)*(1-exp(-pi)), lambda x: exp(-x)*sin(4*x), 0, pi)

print '\nFor (d), there is not much decrease in error. Error ratio is increasing very slowly.'
