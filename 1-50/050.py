from euler import primes

def consec_primes(xx):
    prime_list = primes(xx)
    maxn = 0
    for ii in range(len(prime_list)):
        ss = kk = 0
        for jj in range(ii,len(prime_list)):
            ss += prime_list[jj]
            kk += 1
            if(ss in prime_list and ss < xx):
                if kk > maxn:
                    maxn = kk 
                    print ss, maxn

consec_primes(100000)