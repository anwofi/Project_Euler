def digits_as_nth_powers(maxn,nn):
    """
    Finds all numbers that can be written as sum of the nn-th power of their digits up to maxn.
    The output is the sum of these numbers.	
    """
    sumtot = 0
    for ii in range(2,maxn):
        iistr = str(ii)
        sumn = 0
        for j in range(len(iistr)):
            sumn += int(iistr[j])**nn	
        if ii == sumn:
            sumtot += ii
    return sumtot

print digits_as_nth_powers(200000,5)
