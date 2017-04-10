#### Lagrage: Q. 3, 4, 5
#### Newton Interpolation
#### Q: 3,7,10 (pg. 182 - 185)

from math import *
from matplotlib import pyplot

## Lagrage
print 'Question 3, pg. 176'
def f(x):
    return 1.0/x

def p(x):
    return (8.0/3)*x*x - 6.0*x + 13.0/3

x_plot = [0.25 + i/100.0 for i in range(101)]
pyplot.figure(1)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,map(f,x_plot))
pyplot.plot(x_plot,map(p,x_plot))
pyplot.show()

print 'Question 4, pg. 176'
def f(x):
    return x**0.5

def p(x):
    return (-32.0/105)*x*x + (22.0/21)*x + 9.0/35

x_plot = [i/100.0 for i in range(201)]
pyplot.figure(2)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,map(f,x_plot))
pyplot.plot(x_plot,map(p,x_plot))

print 'Question 5, pg. 176'
def f1(x):
    return log(x)

def p1(x):
    return (-0.235566)*x*x - 1.399845*x - 1.164279

def f2(x):
    return x**0.5

def p2(x):
    return (-1.0/6)*x*x + (7.0/6)*x

def f3(x):
    return log(x,2)

def p3(x):
    return (-1.0/6)*x*x + (3.0/2)*x - (4.0/3)

def f4(x):
    return sin(pi*x)

def p4(x):
    return 0

x_plot = [i/100.0 for i in range(1,501)]
pyplot.figure(3)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,map(f1,x_plot))
pyplot.plot(x_plot,map(f2,x_plot))
pyplot.plot(x_plot,map(f3,x_plot))
pyplot.plot(x_plot,map(f4,x_plot))

pyplot.plot(x_plot,map(p1,x_plot))
pyplot.plot(x_plot,map(p2,x_plot))
pyplot.plot(x_plot,map(p3,x_plot))
pyplot.plot(x_plot,map(p4,x_plot))

## Error
def get_error(x,f,p):
    a = f(x[0])
    b = p(x[0])
    error = [abs(a-b)]
    for i in range(1,len(x)):
        a = f(x[i])
        b = p(x[i])
        error.append(abs(a-b))
    return error

x_plot = [i/100.0 for i in range(1,501)]
pyplot.figure(4)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot,get_error(x_plot,f1,p1))
pyplot.plot(x_plot,get_error(x_plot,f2,p2))
pyplot.plot(x_plot,get_error(x_plot,f3,p3))
pyplot.plot(x_plot,get_error(x_plot,f4,p4))


###### Newton Interpolation
def calculate_coefficients(x,y):
    a = [y[0]]
    for k in range(1,len(x)):
        w = 1
        p = 0
        for j in range(k):
            p = p + a[j]*w
            w = w*(x[k] - x[j])
        a.append((y[k] - p)/w)   # add items to the list
    return a

def evaluate_polynomial(xx, x, a):
    px = a[-1] #last thing in the array
    
    for k in range(len(a)-2,-1,-1):
        xd = xx - x[k]
        px = a[k] + (px * xd)
    
    return px

print 'Question 3, pg. 182'

def f(x):
    return exp(x)

nodes = [2.0, 4.0, 8.0, 16.0, 32.0]

def max_error(nodes, f, p, a):
    new_max = abs(f(nodes[0]) - p(nodes[0],nodes,a))
    maximum = new_max
    for i in range(1,501):
        prev_max = new_max
        new_max = abs(f(nodes[-1+2*i/500])-p(nodes[-1+2*i/500],nodes,a))
        if new_max > prev_max:
            maximum = new_max
    return maximum

def get_en(f,p):
    n = [2,4,8,16,32]
    b = -1
    maximum = [0]
    for i in range(5):
        diff = 2.0/n[i]
        nodes = [b]
        for j in range(1,n[i]+2):
            nodes.append(nodes[j-1]+diff)
        y_values = map(f, nodes)
        a = calculate_coefficients(nodes,y_values)
        if i == 0:
            maximum[0] = max_error(nodes, f, p, a)
        else:
            maximum.append(max_error(nodes, f, p, a))
    return maximum

x_plot = nodes

pyplot.figure(5)
pyplot.ion()
pyplot.clf()
pyplot.plot(x_plot, get_en(f, evaluate_polynomial))


print
print 'Question 7, pg. 183'

nodes = [0.0, 1.0/2, 3.0/4, 5.0/4]
y_values = [0.0, 49.4, 73.0, 119.4]
a = calculate_coefficients(nodes, y_values)
print a

nodes = [0.0,1.0/4,1.0/2, 3.0/4,1.0, 5.0/4]
y_values = [0, 25.0,49.4,73.0,96.4,119.4]
a = calculate_coefficients(nodes, y_values)
print a

print
print 'Question 10, pg. 184'

### a
nodes = [0.0, 1.0/2, 1.0]
y_values = [0.0, 0.52049987781305, 0.84270079294971]
a = calculate_coefficients(nodes, y_values)
print 'a: coeffiecients', a

x_plot = [i/100.0 for i in range(101)]
pyplot.figure(6)
pyplot.ion()
pyplot.clf()
pyplot.plot([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],\
            [0.0,0.11246291601828,0.22270258921048,0.32862675945913,0.42839235504667,\
             0.52049987781305,0.60385609084793,0.67780119383742, 0.74210096470766,\
             0.79690821242283,0.84270079294971],'ro')
pyplot.plot(x_plot, [evaluate_polynomial(xx, nodes, a) for xx in x_plot], '--')

## b
nodes = [0.0,0.3,0.7,1.0]
y_values=[0.0, 0.32862675945913, 0.67780119383742, 0.84270079294971]
a = calculate_coefficients(nodes, y_values)
print 'b: coeffiecients', a
pyplot.plot(x_plot, [evaluate_polynomial(xx, nodes, a) for xx in x_plot],'--')

print 'For (a), error is smaller at ends and in the middle.'
print 'For (b), error is smaller than (a), error is smallest at the ends and in the middle.'
