#! /usr/bin/python
# -*- coding: utf-8 -*- 

def namescore(xx):
    """
    Gives the Score of a single name. The Score is the sum of the indexes of the respective letters in the alphabet.
    """
    sum = 0
    for ii in xx:
        sum += ord(ii) - 64
    return(sum)

def namesscore(xx):
    """
    Gives the score of names read from the file xx.
    """
    inp = open(xx,"r").read().replace("\"","").split(",")
    sum = 0
    for ii in range(0, len(inp)):
        sum += (ii + 1) * namescore(inp[ii])
    return(sum)

print(namesscore("names.txt"))
