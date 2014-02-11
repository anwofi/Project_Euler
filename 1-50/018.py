#! /usr/bin/python
# -*- coding: utf-8 -*- 

def path_sum(xx):
    file = open(xx,"r").read().split("\n")
    data = [map( int, ii.split()) for ii in file]
    ll = len(data)-1 
    for ii in range(ll,-1,-1):
        ll2 = len(data[ii]) - 1
        for jj in range(ll2):
            data[ii-1][jj] += max(data[ii][jj], data[ii][jj+1])
    return max(data)
    
print path_sum("018.txt")