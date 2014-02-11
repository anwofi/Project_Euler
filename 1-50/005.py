#! /usr/bin/python
# -*- coding: utf-8 -*- 

def gcd(aa, bb):
    """
    Gives the gcd of aa and bb.
    """
    if min(aa, bb) == 0:
        out = max(aa, bb) 
    else:
        out = gcd(min(aa, bb), max(aa, bb) % min(aa, bb))
    return(out)

def gcf(aa, bb):
    """
    Gives the greatest common factor of aa and bb.
    """
    return(int(aa * bb / gcd(aa, bb)))

def divisors(xx, out = 1):
    """
    Gives the greatest common factor from 1 up to xx.
    """
    for ii in range(1, xx):
        out = gcf(out, ii)
    return(out)

print(divisors(20))
