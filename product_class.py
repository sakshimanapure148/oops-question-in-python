# Question 12: Product Class
# Create a Product class with product name, price, and quantity.
# Calculate the total price using a method.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display(self):
        print("Product Name:", self.name)
        print("Price per item: ₹", self.price)
        print("Quantity:", self.quantity)
        print("Total Price: ₹", self.calculate_total_price())


if __name__ == "__main__":
    product1 = Product("Notebook", 50, 4)
    product1.display()
