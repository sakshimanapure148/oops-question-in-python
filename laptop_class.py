# Question 11A: Laptop Class
# Create a Laptop class with brand and RAM attributes.
# Use display() to show the laptop details.

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram, "GB")


if __name__ == "__main__":
    laptop1 = Laptop("Dell", 16)
    laptop1.display()
