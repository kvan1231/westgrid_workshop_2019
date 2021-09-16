from math import pi

n = 10000000000
h = 1./n
sum = 0.

for i in range(n):
    x = h * ( i + 0.5 )
    sum += 4. / ( 1. + x**2)

sum *= h
print(sum, abs(sum-pi))
