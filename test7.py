##import time,threading
##def loop():
##    print('thread %s is running...' % threading.current_thread().name)
##    n = 0
##    while n < 5:
##        n = n + 1
##        print('thread %s >>> %s' % (threading.current_thread().name, n))
##        time.sleep(1)
##    print('thread %s ended.' % threading.current_thread().name)
##
##print('thread %s is running...' % threading.current_thread().name)
##t=threading.Thread(target=loop,name='LoopThread')
##t.start()
##t.join()
##print('thread %s ended...' % threading.current_thread().name)

import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt_time=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    m=re.match(r'^UTC([\+,-])(0?[0-9]|1[0-2])\:00$',tz.str)
    tz=int(m.group(1)+m.group(2))
    dt=timezone(timedelta(hours=tz))
    dt_ts=dt.timestamp()
    
