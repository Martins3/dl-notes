#!/usr/bin/env python
a = [1, 2, 3, 4]
print(list(reversed(a)))
print("{a} and {b}".format(a = 1, b = 2))

def switch(x):
    return {1: "a",
            2: "b",
            3: "d"}.get(x, "somehint out of control")

for i in range(5):
    print(switch(i))


assert 1 < 2 , "the 1 is same as 2"

a = 1
b = 2
a, b = b, a
print(a ,b)
