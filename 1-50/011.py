#! /usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np

def grid_product(xx):
    """
    Loads a grid of integer below 100 from a file xx. The output is the greatest product of
    4 adjacent numbers.
    """
    data = np.loadtxt(xx,dtype=np.int16)
    ll = len(data)
    out = 0
    rr = xrange(4)
    for ii in range(ll):
        for jj in range(ll):
            if(jj + 3 < ll):
                bb = 1
                for kk in rr:
                    bb *= data[ii][jj + kk]
            if(ii + 3 < ll):
                cc = 1
                for kk in rr:
                    cc *= data[ii + kk][jj]
            if(ii + 3 < ll and jj + 3 < ll):
                dd = 1
                for kk in rr:
                    dd *= data[ii + kk][jj + kk]
            if(ii + 3 < ll and jj - 3 < ll):
                ee = 1
                for kk in rr:
                    ee *= data[ii + kk][jj - kk]
            for kk in (bb,cc,dd,ee):
                out = max(out, kk)
    return out

print grid_product("011.txt")