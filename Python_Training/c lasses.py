class Calculator:
    def add(self, x, y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def division(self,x,y):
        if y!=0:
            return x/y
        else:
            return ("Cannot divide by zero!")
        
Calculator = Calculator()
results = Calculator.add(8,4)
print(f"8 + 4 = {results}")

results = Calculator.subtract(3,4)
print(f"3 - 4 = {results}")


results = Calculator.multiply(6,7)
print(f"6 * 7 = {results}")

results = Calculator.division(20,0)
print(f"20 / 0 = {results}")