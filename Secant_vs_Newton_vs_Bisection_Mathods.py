from math import *
import math

def secant(f,x0, x1, epsilon):
    """Use the secant method to find a root of the function f.
        x0 and x1 are the initial guesses of the root.
        Interation continues until the difference between x_k+1 and x_k is less than epsilon."""
    
    f0 = float(f(x0))
    f1 = float(f(x1))
    n = 1
    while abs(x1 - x0) >= epsilon:
        n += 1
        x2 = x1 - f1*(x1 - x0)/(f1-f0)
        x0, x1 = x1, x2
        f0, f1 = f1, f(x1)
    return x2

def bisection(f, a, b, eps):
    fa = f(a)
    fb = f(b)
    if f(a)*f(b) > 0 :
        return
    n = (math.log(b-a) - math.log(eps))/(math.log(2))
    n = int(n)
    for i in range(n):
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

def newton(f, fp, x0, eps):
    if fp(x0) == 0:
        return
    x1 = x0 - f(x0)/fp(x0)
    i = 1
    while abs(x1 - x0) >= eps:
        i += 1
        x0 = x1
        fp0 = fp(x0)
        if i > 1000:
            return
        if fp0 == 0:
            return
        x1 = x0 - f(x0)/fp0

    x0 = x1
    return x0

if __name__ == '__main__':
    
    a = secant(lambda x: x**3 - 2, 0, 2, 1.0e-6)
    b = secant(lambda x: exp(x) - 2, 0, 1, 1.0e-6)
    c = secant(lambda x: x - exp(-x), 0, 1, 1.0e-6)
    d = secant(lambda x: x**6 - x - 1, 0, 2, 1.0e-6)
    e = secant(lambda x: x**3 - 2*x - 5, 0, 3, 1.0e-6)
    f = secant(lambda x: 1 - 2*x*exp(-x/2), 0, 2, 1.0e-6)
    g = secant(lambda x: 5 - x**(-1), 0.1, 0.25, 1.0e-6)
    h = secant(lambda x: x*x - math.sin(x), 0, math.pi, 1.0e-6)
    
    print "a: %.3f \nb: %.3f \nc: %.3f \nd: %.3f \ne: %.3f \nf: %.3f \ng: %.3f \nh %.3f" \
    % (a,b,c,d,e,f,g,h)
    
    a_bisection = bisection(lambda x: x**3 - 2, 0, 2, 1.0e-6)
    b_bisection = bisection(lambda x: exp(x) - 2, 0, 1, 1.0e-6)
    c_bisection = bisection(lambda x: x - exp(-x), 0, 1, 1.0e-6)
    d_bisection = bisection(lambda x: x**6 - x - 1, 0, 2, 1.0e-6)
    e_bisection = bisection(lambda x: x**3 - 2*x - 5, 0, 3, 1.0e-6)
    f_bisection = bisection(lambda x: 1 - 2*x*exp(-x/2), 0, 2, 1.0e-6)
    g_bisection = bisection(lambda x: 5 - x**(-1), 0.1, 0.25, 1.0e-6)
    h_bisection = bisection(lambda x: x*x - math.sin(x), 0, math.pi, 1.0e-6)
    
    a_newton = newton(lambda x: x**3 - 2, lambda x: 3*x*x, 0, 1.0e-6)
    b_newton = newton(lambda x: exp(x) - 2, lambda x: exp(x), 0, 1.0e-6)
    c_newton = newton(lambda x: x - exp(-x), lambda x: 1 + exp(-x), 0, 1.0e-6)
    d_newton = newton(lambda x: x**6 - x - 1, lambda x: 6*x**5 - 1, 0, 1.0e-6)
    e_newton = newton(lambda x: x**3 - 2*x - 5, lambda x: 3*x*x - 2, 0, 1.0e-6)
    f_newton = newton(lambda x: 1 - 2*x*exp(-x/2), lambda x: (x - 2)*exp(-x/2), 0, 1.0e-6)
    g_newton = newton(lambda x: 5 - x**(-1), lambda x: x**(-2), 0.1, 1.0e-6)
    h_newton = newton(lambda x: x*x - math.sin(x), lambda x: 2*x - math.cos(x), 0, 1.0e-6)
    
    print '\nResults for secant, bisection and newton mothods'
    
    print 'Q.','secant  |', 'bisection', ' | newton'
    print 'a: %.5f | %.5f    | ' % (a,a_bisection),a_newton
    print 'b: %.5f | %.5f    | %.5f ' % (b, b_bisection, b_newton)
    print 'c: %.5f | %.5f    | %.5f ' % (c, c_bisection, c_newton)
    print 'd: %.5f| %.5f    | ' % (d,d_bisection), d_newton
    print 'e: %.5f | %.5f    | %.5f ' % (e, e_bisection, e_newton)
    print 'f: %.5f | %.5f    | %.5f ' % (f, f_bisection, f_newton)
    print 'g: %.5f | %.5f    | %.5f ' % (g, g_bisection,g_newton)
    print 'h: %.5f | %.5f    | %.5f ' % (h, h_bisection,h_newton)
    
    print
    print "In question a, newton's methos doesn't work because of zero division",\
    "(x0 = 0 gives f'(0) = 0)"
    print "In question d and h, secant method bisection method gives two different",\
    "roots. Both of them are correct. Newton's method doesn't work for d because it is a infinite loop."
    print "In most of other questions secant and newton's mothods give similar answers except question e."

