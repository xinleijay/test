from numpy import *
while True:
    (cn, cw, ch) = (int(x) for x in raw_input().split())
    ew = [0 for i in range(cn)]
    eh = [0 for i in range(cn)]
    res = [0 for i in range(cn)]
    result = []
    wid = []
    hid = []
    sortedid = []
    ww = {}
    hh = {}
    count = 0
    plus = 0
    flag = 0
    for i in range(cn):
        (ew[i], eh[i]) = (int(x) for x in raw_input().split())
        if ew[i] > cw and eh[i] > ch:
            res[i] = [ew[i], eh[i]]
            if res[i][0] not in result or res[i][1] not in result:
                count += 1
                wid.append(res[i][0])
                hid.append(res[i][1])
        else:
            plus += 1
    ww = array(wid).argsort()
    hh = array(hid).argsort()
    if count == 0:
        print '0'
        print '0'
        continue
    else:
        for i in range(count):
            if ww[i] == hh[i]:
                for j in range(count):
                    if (i != j and wid[ww[i]] == wid[ww[j]]) or (i != j and hid[ww[i]] == hid[ww[j]]):
                        flag = 1
                        break
                if flag == 0 or ww[j] not in sortedid:
                    sortedid.append(ww[i])
            else:
                if (ww[i]) not in sortedid and (hh[i]) not in sortedid:
                    sortedid.append(min(ww[i], hh[i]))
        print len(sortedid)
    for i in range(len(sortedid)):
        print (sortedid[i]+plus+1),

