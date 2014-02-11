maxl = 0
for nn in range(2,1000):
    
    ss = 1
    num = []
    for ii in range(1000):
        while ss < nn:
            ss *= 10
        rr = ss / nn
        ss %= nn
        num += [rr]
        if ss == 0:
            break
    if ss != 0:
        while len(num) < 1000:
            num += [0]
        cycle = []
        tmp = []
        jj = 0
        while tmp[:1000] != num[:1000]:
            cycle += [num[jj]]
            tmp = cycle[:]
            while len(tmp) < 1000:
                tmp += cycle
            #print tmp
            jj += 1
        if len(cycle) < 999 and maxl < len(cycle):
            maxl = len(cycle)
            print nn, "length: ", maxl#,cycle