import sys
"""
如果比较相同的对象实例，is总是返回True 而 == 最终取决于 "eq()"
"""

class foo(object):
    def __eq__(self, other):
        return True
f = foo()
print(f == None)
print(f is None)
# we didn't understand the reason why  f is None

# find the IndexError
ints = [1, 2, 3, 4]
for idx, val in enumerate(ints):
    print(idx, val)


# other form for swith
def f(x):
    return{"a":1,"b":2,}.get(x, 9)

print(f(1))
print(f("a"))

# test a function for myself about
class TestClass(object):

    attr_name = 12
    def __init__(self):
        print("i don't know how to use init in python")

m = TestClass()
gvar = 12
if(False):
    lvar = 12
if 'lvar' in locals():
    # myVar exists.
    print("myvar is in the local")

if 'gvar' in globals():
    print("myVar is in the globlas")

if hasattr(m, 'attr_name'):
 # obj.attr_name exists.
 print("the object has the attr")


#?: in python
print("the first one "if 1 > 2 else "this second")

sys.exit()

# with



# __future__

## 1 absolute import
### 1.1
from .sister import foo
import .brother
from ..aunt import bar
import ..uncle
### 1.2
def sin_degrees(x):
    from math import *
    return sin(degrees(x))
    # 不允许， 仅仅一下可以
def sin_degrees(x):
    from math import sin, degrees
    return sin(degrees(x))

from math import *
def sin_degrees(x):
    return sin(degrees(x))

## division
"""
https://stackoverflow.com/questions/2958684/python-division
Python 2.x 对于整数的除法使用的为truncated 政策，但是Python 3.x 使用的原则默认小数
使用 form __future__ import division 就是无论编译器是哪一个版本，都是使用Python 3.x 的原则的
"""
## print_function
"""
just bring the  python 3.x print(), so there is no SyntaxError for print(1)
"""
# gzip file
## 用于读取 gzip格式压缩的文件
import gzip
with gzip.open('input.gz','r') as fin:
            for line in fin:
                print('got line', line)


# @property
