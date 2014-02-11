#! /usr/bin/python
# -*- coding: utf-8 -*- 

from math import factorial

def digitsum_fac(xx, sum = 0):
    """
    Gives the sum of digits of xx!.
    """
    inp = str(factorial(xx))
    for ii in inp:
        sum += int(ii)
    return sum
    
print digitsum_fac(100)