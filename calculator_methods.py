# Question 11B: Calculator Class
# Create a Calculator class with two numbers.
# Add methods for addition, subtraction, and multiplication.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2


if __name__ == "__main__":
    calculator1 = Calculator(20, 5)
    print("Addition:", calculator1.addition())
    print("Subtraction:", calculator1.subtraction())
    print("Multiplication:", calculator1.multiplication())
