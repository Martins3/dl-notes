class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()


class Net():
    def __init__(self):
        self.name = "ResNet"
        print(self)
    i = 0

ChildA()
ChildB()
a = Net()
print(a.i)
print(a.name)
a.error = 1
b = Net()
# print(b.error)
