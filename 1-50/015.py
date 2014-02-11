#! /usr/bin/python
# -*- coding: utf-8 -*- 

from math import factorial
 
def binom(nn,kk):
	return (factorial(nn)/(factorial(kk)*factorial(nn-kk)))
 
print binom(40,20)
