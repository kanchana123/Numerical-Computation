# This script investigates the error in approximating exp(x) by 1 + x
# as x approches zero.  This error is O(x^2).

from math import exp

x = 1.0
previous_error = exp(x) - (1+x)

for i in range(10):
    x = x / 2
    error = exp(x) - (1+x)
    ratio = previous_error / error
    print x, error, ratio
    previous_error = error
