#!/usr/bin/python
# -*- coding: utf-8 -*- 

def col_length(xx):
    """
    Gives the length of a collatz sequence starting at xx.
    """
    yy = 1
    while xx > 1:
        if xx % 2 == 0:
            xx /= 2 
        else:
            xx = 3 * xx + 1
        yy += 1
    return(yy)

def find_lcol(xx):
    """
    Finds the longest collatz sequence with starting numbers below xx. 
    """
    yy = zz = 0
    for ii in range(1,xx-1):
        tmp = col_length(ii)
        if tmp > yy:
             yy = tmp
             zz = ii 
    return(zz)

print find_lcol(1000000)
