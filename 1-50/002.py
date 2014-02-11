#! /usr/bin/python
# -*- coding: utf-8 -*- 
def fibsum(xx):
    f1 = 0
    f0 = 1
    fibs = set()
    while f1 <= xx:
        tmp = f0
        f0 += f1
        f1 = tmp
        if f0 % 2 == 0:
            fibs.add(f0)
    return(sum(fibs))

print fibsum(4e+6)