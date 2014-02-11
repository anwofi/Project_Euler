#! /usr/bin/python
# -*- coding: utf-8 -*- 

def fib_digits(xx):
    f1 = ll = 0
    f0 = 1
    fibs = []
    while ll < xx :
        tmp = f0
        f0 += f1
        f1 = tmp
        fibs += [f0]
        ll = max(ll, len(str(f0)))
    return len(fibs) + 1 

print fib_digits(1000)
