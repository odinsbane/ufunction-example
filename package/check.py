#!/usr/bin/env python3

import numpy
import sys


def fun1(x, y):
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

numpy.random.seed(1)
x = numpy.random.random((10000, 10000))
y = numpy.random.random((10000, 10000))

for i in range(5):
    x = fun3(x,y)

print(sum(sum(x)))

