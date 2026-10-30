# Question 12: Product Class
# Create a Product class with product name, price, and quantity.
# Calculate the total price using a method.

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_details(self):
        total_price = self.calculate_total_price()

        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", total_price)


# Create an object of the Product class
product1 = Product("Notebook", 50, 4)

# Display product details and total price
product1.display_details()
