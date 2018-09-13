#!/usr/bin/env python3

import numpy
import package.ufunny as ufunny          

numpy.random.seed(1)
x = numpy.random.random((10000, 10000))
y = numpy.random.random((10000, 10000))

for i in range(5):
    x = ufunny.funny(x,y)

print(sum(sum(x)))
