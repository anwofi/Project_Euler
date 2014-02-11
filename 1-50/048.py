def power_series(xx):
    outp = 0
    for ii in range(1,xx):
        outp += ii**ii
    return(outp%10000000000)

print power_series(1000)
