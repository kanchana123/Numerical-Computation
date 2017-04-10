from math import *
import math
import copy


def solve(l,d,u,f):
    n = len(f)
    d = map(float,d)
    
    for row in range(1,n):
        d[row] = d[row] - u[row-1] * l[row] / d[row-1]
        f[row] = f[row] - f[row-1] * l[row] / d[row-1]
    
    f[n-1] = f[n-1] / d[n-1]

for row in range(n-2, -1,-1):
    f[row] = (f[row] - u[row] * f[row+1]) / d[row]
    
    return f

def multiply(l, d, u, x):
    row, n = 0, len(x)
    product = [d[row]*x[row] + u[row]*x[row+1]]
    
    for row in range(1, n-1):
        product.append(l[row]*x[row-1] + d[row]*x[row] + u[row]*x[row+1])
    
    row = n -1
    product.append(l[row]*x[row-1] + d[row]*x[row])
    
    return product

####### Question 1 - Exercise 2 on page 83
print "****** Question 1 *******"
u = [2,1,1,1]
d = 4*[4.0]
l = [1,1,1,2,]

f = [math.pi/9, (3**0.5)/2 ,(3**0.5)/2 ,(-1)*math.pi/9]
copy_of_f = copy.copy(f)

x = solve(l,d,u,f)

y = multiply(l,d,u,x)

print 'x =', x
print 'y =', y
print 'f =', copy_of_f

residual = [f - yy for (f, yy) in zip(copy_of_f, y)]
print 'residual =', residual

####### Question 2 - Exercise 7 on page 83
print
print "******* Question 2 ******"

def check_diagonal_dominance(l,d,u,f):
    n = len(f)
    is_dominant = 1
    for row in range(0,n):
        if (d[row] <= (u[row] + l[row])) or ((u[row] + l[row])  <= 0):
            is_dominant = 0

return is_dominant

u = [0.5,0.25,1.0/6.0,0]
d = [1.0,1.0/3.0,1.0/5.0,1.0/7.0]
l = [0,0.5,0.25,1.0/6.0]

f = [2.0, 23.0/12.0, 53.0/30.0 , 15.0/14.0]
copy_of_f = copy.copy(f)

if(check_diagonal_dominance(l,d,u,f) == 0):
    print "This matrix is NOT diagonally dominant."
else:
    print "This matrix is diagonally dominant."

x = solve(l,d,u,f)

y = multiply(l,d,u,x)

print "Exercise 7"
print 'x =', x
print 'y =', y
print 'f =', copy_of_f

residual = [f - yy for (f, yy) in zip(copy_of_f, y)]
print 'residual =', residual

#### Exercise Q-6
u = [0.5,0.25,1.0/6.0,0]
d = [1.0,1.0/3.0,1.0/5.0,1.0/7.0]
l = [0,0.5,0.25,1.0/6.0]

f = [2.0, 2.0, 53.0/30.0 , 15.0/14.0]
copy_of_f = copy.copy(f)

x = solve(l,d,u,f)

y = multiply(l,d,u,x)

print
print "Exercise Q.6"
print 'x =', x
print 'y =', y
print 'f =', copy_of_f

residual = [f - yy for (f, yy) in zip(copy_of_f, y)]
print 'residual =', residual
print "Residual is 0. value of x3 and x4 is different."

###### Question 3 - Exercise 11 page 84
print
print "******* Question 3 ******"

u = 10*[1.0]
l = 10*[1.0]

d = [2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0]

f = 10*[1.0]
copy_of_f = copy.copy(f)

x = solve(l,d,u,f)

y = multiply(l,d,u,x)

print 'x =', x
print 'y =', y
print 'f =', copy_of_f

residual = [f - yy for (f, yy) in zip(copy_of_f, y)]
print 'residual =', residual

###### Question 4 - Exercise 12 page 84
print
print "******** Question 4 ******"

def solve_penta(u1,u,l1,l,d,f):
    n = len(f)
    
    #### making l1 all zeroes
    for row in range(2,n):
        l[row] = l[row] - d[row-1] * l1[row] / l[row-1]
        d[row] = d[row] - u[row-1] * l1[row] / l[row-1]
        u[row] = u[row] - u1[row-1] * l1[row] / l[row-1]
        f[row] = f[row] - f[row-1] * l1[row] / l[row-1]
    
    ###### making l all zero
    for row in range(1,n):
        d[row] = d[row] - u[row-1] * l[row] / d[row-1]
        u[row] = u[row] - u1[row-1] * l[row] / d[row-1]
        f[row] = f[row] - f[row-1] * l[row] / d[row-1]


    f[n-1] = f[n-1] / d[n-1]
    f[n-2] = (f[n-2] - u[n-2] * f[n-1])/d[2]

for row in range(n-3, -1,-1):
    f[row] = (f[row] - u[row] * f[row+1] - u1[row]*f[row+2]) / d[row]
    
    return f

def penta_multiply(u1,u,l1,l,d,x):
    row, n = 0, len(x)
    product = [d[row]*x[row] + u[row]*x[row+1] + u1[row]*x[row+2]]
    row = 1
    product.append(l[row]*x[row-1] + d[row]*x[row] + u[row]*x[row+1] + u1[row]*x[row+2])
    
    
    for row in range(2, n-2):
        product.append(l1[row]*x[row-2] + l[row]*x[row-1] + d[row]*x[row] + u[row]*x[row+1] + u1[row]*x[row+2])
    
    row = n - 2
    product.append(l1[row]*x[row-2] + l[row]*x[row-1] + d[row]*x[row] + u[row]*x[row+1])
    
    row = n - 1
    product.append(l1[row]*x[row-2] + l[row]*x[row-1] + d[row]*x[row])
    
    return product

u = [2.0, 1.0, 1.0, 0]
u1 = [1.0,1.0, 0, 0]
l = [0,1.0,1.0, 2.0]
l1 = [0, 0, 1.0, 1.0]
d = 4*[4.0]
f = 4*[1]
copy_of_f = copy.copy(f)

x = solve_penta(u1,u,l1,l,d, f)
y = penta_multiply(u1,u,l1,l,d,x)

print 'x =', x
print 'y =', y
print 'f =', copy_of_f

residual = [f - yy for (f, yy) in zip(copy_of_f, y)]
print 'residual =', residual

##### Question 5 - Exercise 4 page 87
print
print "****** Question 5 *****"

def solve_bvp(exact_solution, ff, n, l, d, u, f_0):
    sol = (n-1) * [1]
    print "h^-1","| max|uk - Uk|"
    print "-----|-----------------"
    for i in range(1,11):
        h = 1.0 / (2**(i+1))
        print "%.4d" % (2**(i+1)),
        for i in range(n-1):
            sol[i] = exact_solution((i+1)*h)
            f_0[i] = h*h*f_0[i]
        
        approximation = solve(l,d,u,f_0)
        y = multiply(l,d,u,approximation)
        
        for i in range(n-1):
            sol[i] = exact_solution((i+1)*h)
        
        for i in range(n-2):
            prev_max = sol[i] - y[i]
            if (sol[i+1] - y[i+1]) >= prev_max:
                prev_max = sol[i+1] - y[i+1]
        
        print " %.11f" %  ((prev_max*prev_max)**0.5)

n = 8
h = 1.0 / n

l = (n-1) * [-1]
d = (n-1) * [2 + h*h]
u = (n-1) * [-1]

f_0 = (n-1) * [1]


print "a:"

def exact_solution_a(x):
    return x*(1-x)*math.exp(-x)

def ff_a(x):
    return 4*math.exp(-x) - 4*x*math.exp(-x)

solve_bvp(exact_solution_a, ff_a, n, l, d, u, f_0)

print
print "b:"
def exact_solution_b(x):
    return math.sin(math.pi*x)

def ff_b(x):
    return ((math.pi**2)+1)*math.sin(math.pi*x)


solve_bvp(exact_solution_b, ff_b, n, l, d,u,f_0)

print
print "c:"
def exact_solution_c(x):
    return math.exp(-x)*math.sin(math.pi*x)

def ff_c(x):
    return ((math.pi**2)*math.sin(math.pi*x) + 2*math.pi*math.cos(math.pi*x))*math.exp(-x)

solve_bvp(exact_solution_c, ff_c, n, l, d,u,f_0)

print
print "d:"
def exact_solution_d(x):
    return x*(1-x)*math.log(x)

def ff_d(x):
    return 3-(1/x)-(x*x-x-2)*math.log(x)

solve_bvp(exact_solution_d, ff_d, n, l, d,u,f_0)

# Question 6 - Exercise 6 page 88
print
print "Question 6"

n = 8
h = 1.0 / n

l = (n-1) * [-1]
d = (n-1) * [2 + h*h]
u = (n-1) * [-1]

f_0 = (n-1) * [1]

def f(x):
    return 2*h*h

for i in range(2,9):
    h = 1.0/(2**i)
    l = 4* [-h - 32]
    d = 4* [2*h + h**3]
    u = 4*[-h + 32]
    
    f = 4*[5*(h**3)/6]
    
    copy_of_f = copy.copy(f)
    
    x = solve(l,d,u,f)
    
    y = multiply(l,d,u,x)
    print "%.4d" % (2**i),
    print 'x =', x
