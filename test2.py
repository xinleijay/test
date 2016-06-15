def del_prime(s):
    if s<4:
        return False
    else:
        for i in range(2,s):
            if s % i == 0:
                return True

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

def log(text):
    if callable(text):
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print 'begin call: ' + text
                func(*args, **kw)
                print 'end call: ' + text
            return wrapper
        return decorator

@log
def  now1():
    print 'hello...'

@log('text')
def now2():
    print 'hi...'

def print_stu(std):
    print('%s:%s' %(std['name'],std['score']))

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

