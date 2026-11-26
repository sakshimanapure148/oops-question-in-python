"""Practice: calculate a product's total price."""

import math


class Product:
    """Represent a product and its available quantity."""

    def __init__(self, product_name, price, quantity):
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("Product name cannot be empty.")
        if (
            isinstance(price, bool)
            or not isinstance(price, (int, float))
            or not math.isfinite(price)
            or price < 0
        ):
            raise ValueError("Price must be a non-negative number.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative whole number.")

        self.product_name = product_name.strip()
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_details(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price per item: Rs. {self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: Rs. {self.calculate_total_price():.2f}")


if __name__ == "__main__":
    product1 = Product("Notebook", 50, 4)
    product1.display_details()
