"""Practice: create a Laptop class and display object details."""


class Laptop:
    """Represent a laptop with a brand and RAM capacity."""

    def __init__(self, brand, ram):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string.")
        if isinstance(ram, bool) or not isinstance(ram, int) or ram <= 0:
            raise ValueError("RAM must be a positive whole number.")

        self.brand = brand.strip()
        self.ram = ram

    def display(self):
        """Print the laptop's details."""
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")


if __name__ == "__main__":
    laptop1 = Laptop("Dell", 16)
    laptop2 = Laptop("Lenovo", 8)

    print("=== LAPTOP DETAILS ===")
    laptop1.display()
    print()
    laptop2.display()
