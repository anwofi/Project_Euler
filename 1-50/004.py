#! /usr/bin/python
# -*- coding: utf-8 -*- 

def palsum(xx,yy):
    pals = set()
    for ii in range(xx,yy):
        for jj in range(ii,yy):
            tmp = str(ii * jj)
            if tmp == tmp[::-1]:
                pals.add(int(tmp))
    return max(pals)

print palsum(100,999)