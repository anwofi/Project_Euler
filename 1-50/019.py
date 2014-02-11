def day(xx):
    """   
    Gives the number of each day og the week.
    """
    dd = ["So","Mo","Di","Mi","Do","Fr","Sa"]
    return dd[xx%7]
    
def leapyear(xx):
    """
    Gives the days a Februar in year xx is long.
    """
    if (1900 + xx) % 400:
        out = 29
    else:
        if x % 4 == 0:
            out = 29
        else:
            out = 28
    return out

ss = tt = 0
aa = []
for ii in range(100):
    bb = [31,leapyear(ii),31,30,31,30,31,31,30,31,30,31]
    for kk in range(len(bb)):
        for ll in range(1,bb[kk]):
            aa.append([ll, day(ss + 1)])
            ss += 1
hh = 0
for ii in range(367,len(aa)-1): # Skip the first year.
    if aa[ii] == [1, "So"]:
        hh += 1  

print hh
