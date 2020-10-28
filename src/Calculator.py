 def addition (num1, num2):
    return num1+ num2


 def subtraction(num1, num2):
     return num1 - num2


 def multiplication(num1, num2):
     return num1 * num2


 def division(num1, num2):
     return num1 / num2


class Calculator:
    result= 0

    def __init__(self):
        x=2+2
        self.result=x
        pass
    def add(self,a,b):
        self.result= addition(a,b)
        return addition(a, b)
    def subtract(self,a,b):
        self.result= subtraction(a,b)
        return subtraction(a, b)
