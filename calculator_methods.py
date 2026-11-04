"""Practice: arithmetic methods inside a Calculator class."""


class Calculator:
    """Perform basic arithmetic on two numbers."""

    def __init__(self, num1, num2):
        for value in (num1, num2):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("Calculator values must be numbers.")

        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.num1 / self.num2


if __name__ == "__main__":
    calculator = Calculator(20, 5)

    print("=== CALCULATOR ===")
    print("Addition:", calculator.addition())
    print("Subtraction:", calculator.subtraction())
    print("Multiplication:", calculator.multiplication())
    print("Division:", calculator.division())
