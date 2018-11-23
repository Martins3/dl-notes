# 将数据进行复制，从而长度增加的
a = [1, 2 ,3]
a = a[:3] * 2
for i in a:
    print(i)

def generateRevealedBoxesData(val):
    """
    return a list whoes elements are list width * hieght
    and all is val 
    val 为 bool 的数值
    """
    BOARDWIDTH = 10
    BOARDHEIGHT = 20
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

boxdata = generateRevealedBoxesData(False)

print(type(boxdata))
for i in boxdata:
    print(i)
