#! /usr/bin/python
# -*- coding: utf-8 -*- 

import collections 
from euler import factors

def triangle_divisors(xx):
    """
    This function finds the first triangle number with over xx divisors.
    """
    tri = tmp = afacs = 0
    while afacs < xx:
        tmp += 1 
        tri += tmp
        pfacs = collections.Counter(factors(tri)).values()
        afacs = 1
        for ii in pfacs:
            afacs *= ii + 1
    return tri

print triangle_divisors(500)