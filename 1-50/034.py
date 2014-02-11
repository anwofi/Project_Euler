from math import factorial

def get_fact_digits(maxn):
    """
    Finds the sum of all numbers below maxn which are 
    equal to the sum of the factorial of their digits.
    """
    s = 0
    for i in range(3,maxn):
        k = 0
        l = str(i)
        for j in range(len(l)):
            k += factorial(int(l[j]))
        if i == k:
            s += k 
    return(s)

print get_fact_digits(100000)
