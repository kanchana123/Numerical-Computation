# This script investigates the error in approximating f'(x) by (f(x+h)-f(x))/h
# as h approches zero.  This error is O(h).

import math

f = math.sin
f_prime = math.cos

x = 1.0
h = 1.0

for i in range(10):
    approximation = (f(x+h)-f(x)) / h
    error = f_prime(x) - approximation
    if i > 0:
      ratio = previous_error / error
      print h, error, ratio
    previous_error = error
    h = h / 2
