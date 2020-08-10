from oopDemo import Calculator

class ChildImp(Calculator):
    num2 = 50
    def __init__(self):
        Calculator.__init__(self, 2, 6)

    def getCompleteData(self):
        return self.num2+self.num+self.summation()

obj2 = ChildImp()
print(obj2.getCompleteData())

