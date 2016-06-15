#第一行输入学习天数和总的时间 第二行到第day+1行输入每天他爸要求他学习的最短时间和最长时间。
#求问他学习的天数和总时间能满足他爸每天的要求吗？yes的话则输出每天的学习时间。
#京东笔试题
from math import *
while True:
    (day,sumtime)=(int(x) for x in raw_input().split())
    mintime=[0 for i in range(day)]
    maxtime=[0 for i in range(day)]
    restime=[0 for i in range(day)]
    for i in range(day):
        (mintime[i],maxtime[i])=(int(x) for x in raw_input().split())
    minsum = sum(mintime)
    maxsum = sum(maxtime)
    if sumtime>maxsum or minsum>sumtime:
        print "No"
        continue
    else:
        print "Yes"
        for i in range(day):
            restime[i]= mintime[i]
        diff=sumtime-minsum
        for i in range(day):
            if(maxtime[i]-mintime[i])<diff:
               restime[i]+= (maxtime[i]-mintime[i])
               diff = diff-(maxtime[i]-mintime[i])
            else:
                restime[i] +=diff
                break
        for i in range(day):  
            print restime[i],
