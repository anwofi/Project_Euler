#! /usr/bin/python
# -*- coding: utf-8 -*- 

from euler import primes
from math import sqrt

def lpfactor(xx):
    """
    Gives the largest prime factor of xx.
    """    
    pp = primes(int(sqrt(xx)))
    for ii in pp[::-1]:
        if xx % ii == 0:
            return(ii)

print lpfactor(600851475143)
