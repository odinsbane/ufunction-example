#!/usr/bin/env python3

import numpy
import ufunny

numpy.random.seed(1)
x = numpy.random.random((10000, 10000))
y = numpy.random.random((10000, 10000))

for i in range(1):
    x = ufunny.funny(x,y)

print(sum(sum(x)))
