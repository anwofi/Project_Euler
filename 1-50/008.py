#! /usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np

def consecutive_product(xx, out = 0):
    """
    Reads a string of numbers and calculates the consecutive product
    of every 4 adjacent numbers. The output is the greatest such number.
    """

    data = ""
    for ii in np.loadtxt(xx,dtype="string"):
        data += ii
    for jj in range(len(data[:-4])):
        prod = 1
        for ii in data[jj:jj+5]:
            prod *= int(ii)
        out = max(prod,out)
    return(out)

print(consecutive_product('008.txt'))
