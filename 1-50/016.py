#! /usr/bin/python
# -*- coding: utf-8 -*- 

def digitsum_p2(xx):
    """
    Gives the sum of digits of th xx-th power of 2.
    """
    ll = 0
    num = str(2**1000)
    for ii in num:
        ll += int(ii)
    return(ll)

print digitsum_p2(1000)
