#!/usr/bin/env python3

import numpy
import sys
import numba

@numba.jit
def fun(x, y):
    return x**3 + x**2*y + x*y**2 + y**3 - 0.1

@numba.jit
def fun3(x,y):
    T = numpy.power(x,3)
    T2 = numpy.power(x, 2)
    numpy.multiply(T2,y,T2)
    numpy.add(T,T2,T)
    numpy.power(y, 2, T2)
    numpy.multiply(x, T2, T2)
    numpy.add(T, T2, T)
    numpy.power(y, 3, T2)
    numpy.add(T, T2, T)
    numpy.add(T, -0.1, T)
    return T

@numba.jit
def fun4(x,y):
    w,h = x.shape
    z = numpy.zeros(x.shape)
    for i in range(w):
        for j in range(h):
            z[i,j] = x[i,j]**3 + x[i,j]**2*y[i,j] + x[i,j]*y[i,j]**2 + y[i,j]**3 - 0.1
    return z

numpy.random.seed(1)
x = numpy.random.random((10000, 10000))
y = numpy.random.random((10000, 10000))

for i in range(5):
    x = fun4(x,y)

print(sum(sum(x)))
