from selenium import webdriver


# driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("I'm by default")

    def getData(self):
        print("here is running a function from the class")

    def summation(self):
        return self.firstNum + self.secondNum + self.num


obj = Calculator(6, 7)
obj.getData()
#print(obj.summation())
#obj.getData()
#print(obj.num)
