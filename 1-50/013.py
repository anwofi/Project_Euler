#! /usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np

def numsum(xx, summe = 0):
    data = np.loadtxt(xx,dtype='string')
    for ii in data:
        summe += int(ii[0:11])
    return str(summe)[0:10]

print numsum("013.txt")