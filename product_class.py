# Question 12: Product Class
# Create a Product class with product name, price, and quantity.
# Calculate the total price using a method.

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = self.price * self.quantity
        return total_price

    def display(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price per item: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: ₹{self.calculate_total_price()}")


if __name__ == "__main__":
    product1 = Product("Notebook", 50, 4)
    product1.display()
