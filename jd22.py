from numpy import *
while True:
    (n,w,h) = (int(x) for x in raw_input().split())
    wi = [0 for i in range(n)]
    hi = [0 for i in range(n)]
    for i in range(n):
        (wi[i],hi[i]) = (int(x) for x in raw_input().split())
    wo = []
    ho = []
    ok = []
    for i in range(n):
        if hi[i] > h and wi[i] > w and (wi[i] not in wo):
            ok.append(i)
            ho.append(hi[i])
            wo.append(wi[i])
    if len(ok) == 0:
        print 0
        print 0
        continue
    wa = array(wo)
    ha = array(ho)
    was = wa.argsort()
    ok_i = []
    ok_i.append(was[-1])
    for i in range(len(wo)-1,0,-1):
        if wa[ok_i[-1]] > wa[was[i-1]] and ha[ok_i[-1]] > ha[was[i-1]]:
            ok_i.append(was[i-1])
    total = len(ok_i)
    print total
    for i in range(total):
        print ok[ok_i[i]]+1,
    
