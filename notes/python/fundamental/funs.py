"""
https://docs.python.org/3/library/functions.html 包含很多内置函数
zip()
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
"""
for a, b in zip([1,2,3],["1","2","3"]):
    print(a)
    print(b)



# 函数的参数列表
def starPara(*a):
    for i in a:
        print(a)


starPara(1, 2, 3, 4)
