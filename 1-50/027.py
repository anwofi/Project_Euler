from euler import primes

def longest_prime_chain(aa, bb, pmax = 1000):
    """
    Generates prime chains of the form n^2 + an + b 
    with a < |aa| and b < |bb|. The output are parameters
    a,b generating the longest chain.
    """
    plist = primes(pmax)
    tmp = 0
    out = 0, 0
    for i in range(-aa, aa):
        for j in range(-bb, bb):
            k = j
            n = 0
            while k in plist:
                n += 1
                k = n * n + i * n + j
            if n > tmp:
                tmp = n
                out = i, j
    return out

res = longest_prime_chain(1000,1000)
print res[0] * res[1]