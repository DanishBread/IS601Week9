import math
import pandas as pd

def addition(num1, num2):
    return num1+ num2

def subtraction(num1, num2):
    return num1- num2

def multiplication(num1, num2):
    return num1* num2

def division(num1, num2):
    return num1/ num2

def square(num1):
    return num1**2

def squareRoot(num1):
    return num1** 0.5


class calculator:
    result = 0

    def __init__(self):
        pass

    def __add__(self, num1, num2):
        self.result = addition(num1, num2)
        return  self.result

    def __sub__(self, num1, num2):
        self.result = subtraction(num1, num2)
        return  self.result

    def __mul__(self, num1, num2):
        self.result = multiplication(num1, num2)
        return  self.result

    def __div__(self, num1, num2):
        self.result = division(num1, num2)
        return self.result

    def __square__(self, num):
        self.result =square(num)
        return self.result

    def __squareRoot__(self, num):
        self.result = math.sqrt(num)
        return self.result

    def read_csv(self,obj):

        data = pd.read_csv(obj)
        data = data.values
        a = []
        b = []
        c = []
        for var in range(len(data)):
            a.append(data[var][0])
            b.append(data[var][1])
            c.append(data[var][2])
        return [a, b,c]




