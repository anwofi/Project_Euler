from euler import factors

def cal():
    running = True
    i = 1
    ll = 4
    while running:
        p1 = factors(i)
        p2 = factors(i+1)
        p3 = factors(i+2)
        p4 = factors(i+3)
        if(len(p1)==ll and len(p2)==ll and len(p3)==ll and len(p4)==ll):
            print i," = ",p1,"\n",i+1," = ",p2,"\n",i+2," = ",p3,"\n",i+3," = ",p4,"\n"
            running = False
        i += 1

cal()