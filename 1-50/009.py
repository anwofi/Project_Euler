#! /usr/bin/python
# -*- coding: utf-8 -*- 

from math import sqrt

def checkem(xx):
    """
    Gives the product of length of sides of a pythagorean triplet with perimeter xx.
    """
    for ii in xrange(1, xx):
        for jj in xrange(ii, xx): 
            for kk in xrange(jj, xx):
                if ii + jj + kk == xx:
                    if sqrt(ii**2 + jj**2) == kk:
                        return(ii * jj * kk)
                        
print(checkem(1000))
