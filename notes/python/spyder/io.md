# format output
1. print(p, q, sep = "fuck")
2.  %[flags][width][.precision]type   
    print("%4d   %#5.8x"%(p,q))
3. format

> "First argument: {0}, second one: {1}".format(47,11)
'First argument: 47, second one: 11'
> "Second argument: {1}, first one: {0}".format(47,11)
'Second argument: 11, first one: 47'
> "Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11)
'Second argument:  11, first one:   47.42'
> "First argument: {}, second one: {}".format(47,11)
'First argument: 47, second one: 11'
arguments can be used more than once:
> "various precisions: {0:6.2f} or {0:6.3f}".format(1.4148)
'various precisions:   1.41 or  1.415'
> "Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058)
'Art:   453,  Price:    59.06'
[more ideas about](http://www.python-course.eu/python3_formatted_output.php)
