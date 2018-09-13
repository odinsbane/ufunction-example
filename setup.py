#!/usr/bin/env python3

'''
    setup.py file for funny.c
    Note that since this is a numpy extension
    we use numpy.distutils instead of
    distutils from the python standard library.

    
'''


def configuration(parent_package='package', top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration
    
    config = Configuration('ufunny',
                            parent_package,
                            top_path)
    config.add_extension('',
                            ['funny.c'])

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration, packages=['package'])
