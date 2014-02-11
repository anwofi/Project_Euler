#! /usr/bin/python
# -*- coding: utf-8 -*- 

from euler import *

def number_of_primes(xx):
    primelist = primes(int(xx))
    return(sum(primelist))

print(number_of_primes(2E+6))
