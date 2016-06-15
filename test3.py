class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
        
    @property
    def age(self):
        return 2015 - self._birth

class Screen(object):
    @property
    def width(self):
        return self.width1
    @property
    def height(self):
        return self.height1

    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        self.width1=value
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        self.height1=value

    @property
    def resolution(self):
        return self.width1*self.height1

import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
print('END')

import pdb
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: {}'.format(s))
    pdb.set_trace()
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
