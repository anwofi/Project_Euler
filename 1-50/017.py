#! /usr/bin/python
# -*- coding: utf-8 -*- 

def letters_count(ii):
    """
    Gives the length of every distinguishable part of a written number below 1000.
    """
    ss = {0:0, 1:3, 2:3, 6:3, 10:3, 3:5, 7:5, 8:5, 40:5, 50:5, 60:5, 4:4, 5:4, 
          9:4, 11:6, 12:6, 20:6, 30:6, 80:6, 90:6, 16:7, 70:7, 100:7, 15:7,
          13:8, 14:8, 19:8, 18:8, 17:9}
    return(ss[ii])


# counts up all possible numbers below 1000, this can certainly be generalized

ss = 0
for jj in range(1,1000):
    ones = jj % 10
    tens = jj % 100
    hundreds = int((jj-tens)/100)
    if jj < 20:
        ss += letters_count(tens)
    elif jj < 100:
        ss += letters_count(tens-ones) + letters_count(ones)
    elif jj < 1000:
        if tens > 19:	
            ss += letters_count(hundreds) + 10 + letters_count(tens-ones) + letters_count(ones)
        else:
            ss += letters_count(hundreds) + 7
            if tens != 0:
                ss += 3 + letters_count(tens)
     
print ss + 11
