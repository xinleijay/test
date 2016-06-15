def rec_area(x,y):
    area=0
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    elif not isinstance(y,(int,float)):
        raise TypeError('bad operand type')
    if x<=0:
        return 'error x must >0'
    elif y<=0:
        return 'error y'
    else:
        area=x*y
    print area

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

def change(s):
    s=s.lower()
    s=s.capitalize()
    return s
def normalize(s):
    return s[0].upper()+s[1:].lower()

def mulit(x,y):
    return x*y
def prod(L):
    return reduce(mulit,L)
        
