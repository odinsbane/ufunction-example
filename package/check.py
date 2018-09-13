#!/usr/bin/env python3

import numpy
import sys





def fun1(x, y):
    """
        Generic function with multiple numpy ufunctions.
    """
    return x**3 + x**2*y + x*y**2 + y**3 - 0.1

def fun3(x,y):
    T = numpy.power(x,3)
    T2 = numpy.square(x)
    numpy.multiply(T2,y,T2)
    numpy.add(T,T2,T)
    numpy.square(y, T2)
    numpy.multiply(x, T2, T2)
    numpy.add(T, T2, T)
    numpy.power(y, 3, T2)
    numpy.add(T, T2, T)
    numpy.add(T, -0.1, T)
    return T

def fun4(x,y):
    """
        element wise version.
    """
    w = len(x)
    h = len(x[0])
    z = [ [0]*w for i in range(h) ]
    for i in range(w):
        for j in range(h):
            z[i][j] = x[i][j]**3 + x[i][j]**2*y[i][j] + x[i][j]*y[i][j]**2 + y[i][j]**3 - 0.1
    return z

numpy.random.seed(1)
x = numpy.random.random((10000, 10000))
y = numpy.random.random((10000, 10000))

for i in range(5):
    x = fun1(x,y)

if isinstance(x, list):
    print(sum(i for r in x for i in r))
else:
    print(sum(sum(x)))

