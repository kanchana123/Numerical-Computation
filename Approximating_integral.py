import math

# Question 1
#   Write a Python function to approximate the integral of a function f over the interval from a to b. The function should have four parameters, f, a, b, and n (the number of intervals to be used in the approximation.) To test your function, call it from inside a loop to reproduce the values in the second column of Table 2.9 on page 72 of the text.

def tnf(f,a,b,n):
    h = 1.0*(b - a)/n
    x = a
    sum = f(x)
    for i in range(1,n):
        x = x + h
        sum = sum + 2*f(x)
    sum = sum + f(b)
    sum = sum*(h/2)
    return sum

def f(x):
    return math.exp(x)

a, b, n = 0, 1, 2

print '   n  |      Tn(f)     |'
print '------+----------------'
for i in range(11):
    print '%4.0f  |  %12.10f  |' % (n, tnf(f,a, b, n))
    n = 2*n


# Question 2
#   Write a Python function that finds an estimate of the maximum of the absolute value of the second derivative of a function f over the interval from a to b.

def g(x):
    return math.exp(-x*x)

def get_max(f,a,b,n):
    h = (1.0)*(b - a)/n
    x = a*(1.0)
    new_max = 0.0
    maximum = 0.0
    for i in range(n+1):
        f_p = (f(x+h)-2.0*f(x)+f(x-h))/(h*h)
        new_max = (f_p**2)**(0.5)
        if maximum <= new_max:
            maximum = new_max
        x = x + h
    return maximum

print
print "Question 2: Approximation of the maximum value of the second derivative is", get_max(g,0,1,100)

# Question 3
#   For this question you are to write a Python function that returns a grid spacing, h, for which we know that the error in approximating the integral using the composite trapezoid rule with a uniform grid is less than a prescribed value.

def get_h(f_max,a,b,error):
    return (12*error/((b-a)*f_max))**(0.5)

m = get_max(g,a,b,100)
print
print "Question 3: The value of h, when the error is equal or smaller than 10^(-3), is", get_h(m,a,b,0.001)

### Exercises ###

def exercises(f, a, b, n):
    t = tnf(f, a, b, n)
    m = get_max(f, a, b, 100)
    h3 = get_h(m, a, b, (10**(-3)))
    h6 = get_h(m, a, b, (10**(-6)))
    print "T(f) = %12.10f,"% (t), "h (10^(-3)) = %12.10f," % (h3), "h (10^(-6)) = %12.10f" % (h6),
    return

# Question 3

def f3(x):
    return x**3

print
print "Question 3: ", exercises(f3, a, b, 4)

# Question 4
a, b, n = 0, 1, 8
def f4(x):
    return 1/((1+(x**4))**(0.5))

print
print "Question 4: ", exercises(f4, a, b, n)

# Question 5
def f5(x):
    return x*(1-x**2)

print
print "Question 5: ", exercises(f5, a, b, n)

# Question 6
def f6(x):
    return math.log(1+x)

print
print "Question 6: ", exercises(f6, a, b, n)

# Question 7
a, b = 1, 2

def f7(x):
    return math.exp(-(x**2))

print
print "Question 7: ", exercises(f7, a, b, n)

